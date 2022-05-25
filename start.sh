#!/bin/bash

rootPath=$(pwd)

while read line || [ -n "$line" ] ; do
  cd "$rootPath"

  mainPath="${line%.java}"
  dirPath="${mainPath%/?*}"
  className="${mainPath##?*/}"

  echo "target: $dirPath"
  echo "className: $className"

  cd "$dirPath"
  echo "compiling..."
  javac *.java

  echo ""
done
