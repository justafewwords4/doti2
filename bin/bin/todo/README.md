# Completar en bash

```
sudo cp todo_completion /etc/bash_completion.d/todo
```

## Or put it somewhere in your home directory and source it from your .bashrc:

```
source todo_completion
```

## Note: If you define an alias (e.g. t) to todo.sh, you need to explicitly enable completion for it, too (also put this into your .bashrc):

```
complete -F _todo t
```

Avoid typing todo.sh every time. Add the following to your ~/.bashrc file (~/.bash_profile for Mac and Cygwin users):

```
alias t='./todo.sh -d /path/to/your/todo.cfg'
```

Allow t to list outstanding tasks Add the following to your ~/.bashrc file (~/.bash_profile for Mac and Cygwin users):

```
export TODOTXT_DEFAULT_ACTION=ls
alias t='./todo.sh -d /path/to/your/todo.cfg'
```

## Para hacer todo más rápidamente

### Para bash

```
echo "" >> ~/.bashrc
echo "# todo.txt config" >> ~/.bashrc
echo "" >> ~/.bashrc
echo "source ~/bin/todo/todo_completion" >> ~/.bashrc
echo "export TODOTXT_DEFAULT_ACTION=ls" >> ~/.bashrc
echo "alias t='~/bin/todo/todo.sh -d ~/bin/todo/todo.cfg'" >> ~/.bashrc
```

### Para zsh

```
echo "" >> ~/.zshrc
echo "# todo.txt config" >> ~/.zshrc
echo "" >> ~/.zshrc
echo "source ~/bin/todo/todo_completion" >> ~/.zshrc
echo "export TODOTXT_DEFAULT_ACTION=ls" >> ~/.zshrc
echo "alias t='~/bin/todo/todo.sh -d ~/bin/todo/todo.cfg'" >> ~/.zshrc
```

