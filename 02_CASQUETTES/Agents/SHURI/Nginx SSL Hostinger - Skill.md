---
name: nginx-ssl-hostinger-vps
description: Configure Nginx reverse proxy with Let's Encrypt SSL on a Hostinger VPS. Covers dual-domain setups, HTTP-01 pitfalls (blocked by Hostinger network), DNS-01 certbot workflow, and certificate renewal automation.
tags: ["nginx", "ssl", "letsencrypt", "certbot", "hostinger", "vps", "reverse-proxy"]
---

# Nginx SSL on Hostinger VPS

Let's Encrypt SSL setup for a Hostinger VPS using Nginx reverse proxy, with DNS-01 challenge (HTTP-01 is blocked at network level).

## Key Findings

- **HTTP-01 challenge FAILS on Hostinger VPS** — Even with nginx stopped and port 80 free, Let's Encrypt receives 404 from the Hostinger network layer. This is NOT a nginx config issue; it's a network-level block by Hostinger.
- **DNS-01 is the only working method** — requires creating a TXT record for `_acme-challenge.<subdomain>` in Hostinger DNS Manager.
- **Certbot v4.0.0** on Debian Trixie — removed flags: `--manual-public-ip-logging-ok`, `--manual-cleanup-command`.
- **No crontab on this VPS** — `cron` is not running, so auto-renewal must be handled differently.
- **Hostinger API** returns error 530 with provided API key — fallback to manual DNS.

## Step-by-Step: Add HTTPS to a New Subdomain

### 1. Configure Nginx

Create `/etc/nginx/sites-available/<name>` with:
- listen 80
- server_name set to your domain
- location `/.well-known/acme-challenge/` serving from `/var/www/certbot`
- location `/` with proxy_pass to `127.0.0.1:<port>`
- Include proxy headers: Upgrade, Connection, Host, X-Real-IP, X-Forwarded-For, X-Forwarded-Proto
- proxy_read_timeout 86400

Enable with: `ln -sf` from sites-available to sites-enabled, then `nginx -t && nginx -s reload`

Create the certbot directory: `mkdir -p /var/www/certbot/.well-known/acme-challenge`

### 2. Generate DNS-01 Challenge Token

Use: `certbot certonly --manual -d your-domain.clyro.fr --preferred-challenges dns --manual-auth-hook '<hook that saves CERTBOT_VALIDATION to /tmp/certbot-token.txt>'`

The hook saves the token to `/tmp/certbot-token.txt`. Check it with `cat`.

### 3. Create DNS TXT Record (Hostinger)

In Hostinger DNS Manager:
- **Type**: TXT
- **Name**: `_acme-challenge.your-subdomain`
- **Value**: (token from step 2)
- **TTL**: 60 or 300

Wait 1-2 minutes for propagation.

### 4. IMPORTANT: Each certbot run generates a NEW token

The token in step 2 is stale by the time you finish step 3. You MUST:
- Create DNS with the LATEST token from `/tmp/certbot-token.txt`
- Then run certbot AGAIN — it generates a new token, you must update DNS again immediately, then certbot will validate against your updated DNS record

Check DNS propagation with: `dig _acme-challenge.your-domain.clyro.fr TXT +short`

### 5. Install the Certificate in Nginx

Once certbot succeeds, certs are at `/etc/letsencrypt/live/your-domain.clyro.fr/`.

Update nginx config for HTTPS:
- Change listen to `443 ssl http2`
- Add ssl_certificate pointing to fullchain.pem
- Add ssl_certificate_key pointing to privkey.pem
- Keep the same proxy_pass location block
- Add a separate server block for HTTP (listen 80) that does a 301 redirect to HTTPS

Then: `nginx -t && nginx -s reload`

## Auto-Renewal

Cron is NOT available on this VPS. Options:
1. **Manual**: Run `certbot renew --manual --preferred-challenges dns` every ~60 days
2. **Hermes cronjob**: Use cronjob tool to schedule renewal every 50 days
3. **acme.sh with DNS API**: Install acme.sh with Hostinger DNS hook for automated renewal (requires working API key)

## Critical: Dual-Domain Setup

When adding a SECOND domain to an existing nginx config (e.g., `client-os.clyro.fr` already exists, adding `hermes-dashboard.clyro.fr`):
- Create a SEPARATE nginx config file for the new domain
- Symlink from sites-enabled
- Test with `nginx -t && nginx -s reload`
- Both domains can proxy to the SAME backend port (e.g., 9119) via `proxy_pass http://127.0.0.1:9119`

## Self-Signed Cert Fallback

When Let's Encrypt rate-limits you (5 failed authorizations/hr for the same domain):
1. Generate self-signed cert:
   ```
   openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/nginx/ssl/<domain>.key \
     -out /etc/nginx/ssl/<domain>.crt \
     -subj "/CN=<domain>" \
     -addext "subjectAltName=DNS:<domain>"
   ```
2. Configure HTTPS in nginx with the self-signed cert
3. Wait for rate limit to expire (~1 hour)
4. Replace with real Let's Encrypt cert via DNS-01

## IMPORTANT: Hostinger Port 443 Interception

When testing HTTPS from the VPS itself (`curl -sk https://domain:443` locally via 127.0.0.1), the correct nginx certificate is returned. BUT from the external IP (`curl -sk https://domain -resolve domain:443:<external_ip>`), a DIFFERENT certificate may be returned (e.g., "TRAEFIK DEFAULT CERT"). This means Hostinger has a network-layer proxy/load balancer intercepting port 443 before it reaches your VPS nginx. In this case:
- The 404 "page not found" (plaintext, not nginx HTML) comes from the intercepting proxy, not your nginx
- HTTP (port 80) works fine — traffic reaches your nginx
- Check Hostinger panel for HTTP proxy / CDN settings that may need to be disabled
- Verify with: `curl -svk https://your-domain 2>&1 | grep "subject:"`

## Pitfalls

- **Token mismatch**: Each certbot command generates a new ACME token. Running certbot, getting token, creating DNS, running certbot again = token changed. Must create DNS with the LATEST token and then immediately validate.
- **Certbot v4.0.0 removed flags**: `--manual-public-ip-logging-ok` and `--manual-cleanup-command` no longer exist.
- **Hostinger API returns 530**: API key may be invalid or expired. Fallback to manual DNS.
- **acme.sh install fails**: No cron available on this VPS. `install --nocron` may also fail. Use `--force` workaround or manual certbot.
- **Let's Encrypt rate limit**: 5 failed authorization attempts per identifier per hour. If hit, must wait ~1 hour before retrying. Use `certbot renew --dry-run` to check.
- **Multiple attempts compound the problem**: Each failed certbot run counts toward the rate limit. Be precise: generate token → wait → update DNS → verify with `dig` → then validate.
