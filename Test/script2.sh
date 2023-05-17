#!/usr/bin/expect -f
set timeout -1
set password "1270"
spawn arduino-cli upload --port=192.168.43.210 --fqbn esp32:esp32:esp32 --input-file Bin2.bin
expect {
	"*Password:*" { send "$password\r" ; exp_continue }
	"*\r\n*" { exp_continue }
	eof
}
