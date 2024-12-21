package main

import (
	"flag"
	"fmt"
	"time"
)

// 默认字符集为小写和大写字母
var charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func main() {
	// 解析命令行参数
	seedPtr := flag.Int("seed", 0, "Random seed")
	lengthPtr := flag.Int("length", 0, "Length of the random string")
	charSetPtr := flag.String("charset", "", "Optional character set to use")
	flag.Parse()

	// 检查命令行参数是否有效
	seed := *seedPtr
	length := *lengthPtr
	if seed == 0 || length == 0 {
		fmt.Println("Usage: go run script.go -seed <seed> -length <length> [-charset <character_set>]")
		return
	}

	// 如果提供了字符集参数，则使用它
	if *charSetPtr != "" {
		charSet = *charSetPtr
	}

	// 生成随机字符串
	randomString := generateRandomString(length, seed, charSet)
	fmt.Println(randomString)
}

// 生成随机字符串的函数
func generateRandomString(length int, seed int, charSet string) string {
	l := len(charSet)
	var result string
	rng := NewSimpleLCG(int64(seed))
	for _ = range length {
		k := int(rng.Next() * float64(l))
		result += string(charSet[k])
	}
	return result
}

type SimpleLCG struct {
	m, a, c, state int64
}

func NewSimpleLCG(seed int64) *SimpleLCG {
	if seed == 0 {
		seed = time.Now().UnixNano()
	}
	return &SimpleLCG{
		m:    4294967296, // 2^32
		a:    1664525,
		c:    1013904223,
		state: seed,
	}
}

func (lcg *SimpleLCG) Next() float64 {
	lcg.state = (lcg.a*lcg.state + lcg.c) % lcg.m
	return float64(lcg.state) / float64(lcg.m)
}
