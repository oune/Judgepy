#!/bin/bash

rootPath=$(pwd)
mkdir -p out

while read line; do
  cd "$rootPath"

  mainPath="${line%.java}"
  dirPath="${mainPath%/?*}"
  className="${mainPath##?*/}"
  outName=`echo $mainPath | tr -d '/' | tr -d '.'`

  echo "target: $dirPath"
  echo "className: $className"
  echo "outPath: $outPath"

  cd "$dirPath"
  echo "compiling..."
  javac *.java && echo "compile success" || echo "compile failed"
  java $className < "$rootPath/testcase/1.txt" >> "$rootPath/out/$outName.txt" && echo "java run success" || echo "java run fail"

  echo ""
done 
