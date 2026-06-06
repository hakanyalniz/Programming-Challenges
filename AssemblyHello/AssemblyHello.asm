section .data
    msg db "Hello, World!", 10      ; 10 is the newline character
    msg_len equ $ - msg

section .text
    global main

main:
    ; Write message to stdout
    mov rax, 1                      ; system call for write
    mov rdi, 1                      ; file descriptor 1 is stdout, used as the first argument to write
    mov rsi, msg                    ; address of string to output for rax
    mov rdx, msg_len                ; number of bytes
    syscall                         ; invoke operating system to do the write

    ; Exit program
    mov rax, 60                     ; system call for exit
    xor rdi, rdi                    ; exit code 0
    syscall