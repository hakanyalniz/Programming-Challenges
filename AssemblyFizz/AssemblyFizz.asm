;---------------------
;  Flat Assembler file
;  x86-64 Linux
;  FizzBuzz using Assembly
;---------------------

section .data
    fizz db "Fizz"
    fizz_len equ $ - fizz 

    buzz db "Buzz"
    buzz_len equ $ - buzz 

    fizzbuzz db "FizzBuzz"
    fizzbuzz_len equ $ - fizzbuzz 

    newline db 10
    
    
        
section .bss
    num_buffer resb 10          ; Reserve 10 bytes of memory for our dynamic counter number string

section .text
    global main

main:
    mov rcx, 1          ; Use RCX as our counter (start at 1)
    
    jmp loop_start
    
loop_start:
    push rcx            ; Shield the counter by saving it on the stack


check_fifteen:
    ; modulo 15 check by division
    mov rax, rcx        ; Move our counter into rax
    xor rdx, rdx        ; Clear rdx to 0
    mov rbx, 15         ; We want to divide by 15
    div rbx             ; Divide rdx:rax by rbx. Remainder drops into RDX

    cmp rdx, 0          ; Is the remainder 0?
    je print_fizzbuzz   ; If true, jump to fizzbuzz and skip the rest

check_three:
    ; modulo 3 check by division
    mov rax, rcx        ; Move our counter into rax
    xor rdx, rdx        ; Clear rdx to 0
    mov rbx, 3          ; We want to divide by 3
    div rbx             ; Divide rdx:rax by rbx. Remainder drops into RDX

    cmp rdx, 0          ; Is the remainder 0?
    je print_fizz

check_five:
    ; modulo 5 check by division
    mov rax, rcx        ; Move our counter into rax
    xor rdx, rdx        ; Clear rdx to 0
    mov rbx, 5          ; We want to divide by 5
    div rbx             ; Divide rdx:rax by rbx. Remainder drops into RDX

    cmp rdx, 0          ; Is the remainder 0?
    je print_buzz
    
    
next_iteration:
    ; If it didn't match 15, 3, or 5, it naturally lands here.
    mov rax, rcx                ; Set up RAX with the counter for division
    xor r8, r8                  ; Clear R8 to track string length

  .divide_loop:                   ; The CPU loops here internally until RAX == 0
    xor rdx, rdx
    mov rbx, 10
    div rbx
    add rdx, 48
    push rdx
    inc r8
    cmp rax, 0
    jne .divide_loop            ; "Call" next iteration of divide if RAX != 0

    mov rbx, r8
    mov rdi, num_buffer
  .pop_loop:                      ; The CPU loops here internally to empty the stack
    pop rdx
    mov [rdi], dl
    inc rdi
    dec rbx
    jnz .pop_loop               ; "Call" next iteration of pop if RBX != 0
    
    
    ; Print the finalized number buffer
    mov rax, 1
    mov rdi, 1
    mov rsi, num_buffer
    mov rdx, r8                 ; R8 holds our dynamic length
    syscall
    
    jmp loop_cleanup    ; Escape! Don't slide into the text blocks.

print_fizzbuzz:
    ; Write message to stdout
    mov rax, 1                      ; system call for write
    mov rdi, 1                      ; file descriptor 1 is stdout
    mov rsi, fizzbuzz               ; address of string to output
    mov rdx, fizzbuzz_len           ; number of bytes
    syscall
    jmp loop_cleanup    ; Escape! Don't slide into the text blocks.

print_fizz:
    ; Write message to stdout
    mov rax, 1                      
    mov rdi, 1                      
    mov rsi, fizz                   
    mov rdx, fizz_len               
    syscall
    jmp loop_cleanup
    
print_buzz:
    ; Write message to stdout
    mov rax, 1                      
    mov rdi, 1                      
    mov rsi, buzz                   
    mov rdx, buzz_len               
    syscall  
    jmp loop_cleanup


loop_cleanup:
    ; Print a newline character so the next number starts clean
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall
    
    pop rcx             ;  Safely restore clean counter from stack
    inc rcx             ;  Increment
    cmp rcx, 101        ;  Check boundaries
    jne loop_start      ;  Loop back up if we aren't done

program_exit:
    ; Cleanly tell Linux we are done so it doesn't segmentation fault
    mov rax, 60         
    xor rdi, rdi        
    syscall