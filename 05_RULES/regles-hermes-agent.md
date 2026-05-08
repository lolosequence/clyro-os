# Regles Hermes Agent

## Commandes sans indentation

Toutes les commandes shell fournies a Laurent doivent etre SUR UNE SEULE Ligne, sans indentation, sans backticks, sans blocs de code multiline. Utiliser `&&` pour chainer les commandes au lieu de retours a la ligne.

### EXEMPLES A FAIRE :
echo hello && echo world
echo -e "line1\nline2\nline3" > file.txt
ls -la /tmp | grep test
mkdir -p ~/.ssh && echo 'Host vps' > .ssh/config

### EXEMPLES A NE PAS FAIRE :
cat > file << 'EOF'
  contenu indente
EOF

```
commande_avec_indentation() {
  echo "indente"
}
```

### Pour les fichiers de config (SSH, etc.) :
Utiliser le redirecteur `>` avec echo -e pour ecrire des fichiers multiline sans heredoc. Exemple : echo -e "ligne1\nligne2\n  indente" > file.txt

### Priorite :
Si une commande ne peut pas etre tapee directement par Laurent dans son terminal Windows/WSL sans copier-coller complexe, la reformater sur une ligne.
