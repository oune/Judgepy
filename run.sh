#!/bin/bash

rootPath=$(pwd)
mkdir -p out
mkdir -p file

while read line; do
  cd "$rootPath"

  mainPath="${line%.java}"
  dirPath="${mainPath%/?*}"
  className="${mainPath##?*/}"
  outName=$(echo "$mainPath" | tr -d '/' | tr -d '.')
  echo "target: $dirPath"
  echo "className: $className"

  cd "$dirPath"
  echo "compiling..."
  javac *.java && echo "compile success" || echo "compile failed"

  for testcase in "$rootPath"/testcase/$1/*; do
    echo "$testcase" >>"$rootPath/out/$outName.txt"
    java "$className" < "$testcase" >>"$rootPath/out/$outName.txt" && echo "case $testcase success" || echo "case $testcase fail"
    echo "" >>"$rootPath/out/$outName.txt"
  done

  echo ""
done
