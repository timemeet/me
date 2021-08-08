package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	// "net"
)

func main() {
	var s string
	for i := 0; i < len(os.Args); i++ {
		s += fmt.Sprintf("%d: %s \n", i, os.Args[i])
	}

	fmt.Println(s)

	//1.3. 查找重复的行
	counts := make(map[string]int)
	input := bufio.NewScanner(os.Stdin)

	for input.Scan() {
		counts[input.Text()]++
		if input.Text() == "end" {
			break
		}
	}

	mjson, _ := json.Marshal(counts)
	mstring := string(mjson)
	fmt.Printf("Read buf is: %s\n", string(mstring))

	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}
