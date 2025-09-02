⸻

🐍 Python – print()

print("Hello, World!")

	•	No boilerplate – just call print().
	•	Can print multiple values separated by commas:

print("Sum:", 5 + 7)


	•	By default, adds a newline at the end. To stop it:

print("Hello", end="")  # no newline


	•	Uses dynamic typing: you can print strings, numbers, lists, etc., without conversion.

👉 Remember: Python is simplest for printing. Great for debugging and fast coding.

⸻

☕ Java – System.out.println()

System.out.println("Hello, World!");

	•	System = built-in class,
out = output stream,
println = print line (adds newline).
	•	For printing without newline:

System.out.print("Hello");


	•	For formatted output (like C’s printf):

System.out.printf("Sum: %d\n", 5 + 7);



👉 Remember: In Java, printing is more formal. File/class names matter. println always adds newline; print does not.

⸻

⚡ Go – fmt.Println()

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

	•	fmt = formatting package.
	•	fmt.Println() = print with newline.
	•	fmt.Print() = print without newline.
	•	fmt.Printf() = formatted output:

fmt.Printf("Sum: %d\n", 5+7)



👉 Remember: Go separates normal print (Print), newline (Println), and format (Printf). Always import fmt.

⸻

🔑 Key Points to Recall
	•	Python: print() is simplest. No need to declare types.
	•	Java: System.out.println() is standard, but file/class rules apply.
	•	Go: Printing always comes via fmt package, with Print, Println, or Printf.
	•	Formatted Output: Java (printf) and Go (Printf) are similar to C. Python uses f-strings:

name = "Rahul"
print(f"Hello, {name}")



⸻

✨ Memory Trick:
	•	Python = print (easy).
	•	Java = System.out.println (longest).
	•	Go = fmt.Println (middle).
