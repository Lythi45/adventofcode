package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
    "time"
)

func main() {
    var cells []int
    file, err := os.Open("tag5.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        str,_:=strconv.Atoi(scanner.Text())
        cells=append(cells,str)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
    pos:=0
    num_jumps:=0
    len_c :=len(cells)
    start:=time.Now()
    for pos>=0 && pos<len_c {
      offset:=cells[pos]
      if offset>=3 {
        cells[pos]-=1
      } else {
        cells[pos]+=1
      }

      pos+=offset
      num_jumps+=1
    }
    elapsed := time.Now().Sub(start)
    fmt.Printf("%f %d\n",elapsed.Seconds(), num_jumps)
}
