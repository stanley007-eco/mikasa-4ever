from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import HexColor

out = "Java_Complete_Exam_Notes_Unit_I_II_III.pdf"

doc=SimpleDocTemplate(
    out, pagesize=A4,
    rightMargin=15*mm,leftMargin=15*mm,
    topMargin=17*mm,bottomMargin=15*mm
)

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="Cover",fontName="Helvetica-Bold",fontSize=22,leading=27,
                           alignment=TA_CENTER,textColor=HexColor("#17365D"),spaceAfter=12))
styles.add(ParagraphStyle(name="Unit",fontName="Helvetica-Bold",fontSize=17,leading=21,
                           textColor=HexColor("#17365D"),spaceBefore=5,spaceAfter=9))
styles.add(ParagraphStyle(name="Topic",fontName="Helvetica-Bold",fontSize=12.5,leading=16,
                           textColor=HexColor("#1F4E79"),spaceBefore=7,spaceAfter=4))
styles.add(ParagraphStyle(name="BodyX",fontSize=9.1,leading=13,spaceAfter=4))
styles.add(ParagraphStyle(name="Key",fontName="Helvetica-Bold",fontSize=8.8,leading=12,
                           textColor=HexColor("#7F6000"),backColor=HexColor("#FFF2CC"),
                           borderColor=HexColor("#D6B656"),borderWidth=.4,borderPadding=5,
                           spaceBefore=3,spaceAfter=6))
styles.add(ParagraphStyle(name="CodeX",fontName="Courier",fontSize=7.3,leading=9.7,
                           leftIndent=6,rightIndent=6,backColor=HexColor("#F5F5F5"),
                           borderColor=HexColor("#CCCCCC"),borderWidth=.3,borderPadding=5,
                           spaceBefore=3,spaceAfter=5))
styles.add(ParagraphStyle(name="NoteX",fontSize=8.7,leading=12.2,
                           backColor=HexColor("#EAF2F8"),borderColor=HexColor("#9CC2E5"),
                           borderWidth=.4,borderPadding=5,spaceBefore=4,spaceAfter=6))

story=[]

def P(text,style="BodyX"):
    story.append(Paragraph(text,styles[style]))
def C(text):
    safe=text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    story.append(Paragraph(safe.replace("\n","<br/>"),styles["CodeX"]))
def K(text):
    P("<b>Exam Point:</b> "+text,"Key")
def T(title):
    P(title,"Topic")
def program(title,code,output):
    T("Sample Java Program — "+title)
    C(code.strip())
    P("<b>Output:</b><br/>"+output.replace("\n","<br/>"),"NoteX")

# Cover
story += [
    Spacer(1,28*mm),
    P("JAVA PROGRAMMING","Cover"),
    P("Complete Exam Notes<br/>Definitions • Simple Explanation • Key Points • Syntax • Programs • Output","Cover"),
    Spacer(1,10*mm),
    P("<b>UNIT I • UNIT II • UNIT III</b>","Cover"),
    Spacer(1,15*mm),
    P("Prepared from the topics visible in the supplied syllabus. Unit III is limited to the visible portion of the uploaded image; missing topics are not guessed.","NoteX"),
    PageBreak()
]

# UNIT I
P("UNIT I — INTRODUCTION TO OOP AND JAVA","Unit")

T("1. Overview of OOP")
P("<b>Definition:</b> Object-Oriented Programming (OOP) is a programming approach in which programs are designed using classes and objects.")
P("<b>Simple Explanation:</b> An object contains data and the methods that operate on that data.")
P("<b>Key Points:</b> Class, Object, Encapsulation, Abstraction, Inheritance and Polymorphism.")
C("""class ClassName {
    dataType variable;

    void methodName() {
        // statements
    }
}""")
program("OOP","""class Student {
    int mark;

    void display() {
        System.out.println("Mark = " + mark);
    }

    public static void main(String[] args) {
        Student s = new Student();
        s.mark = 90;
        s.display();
    }
}""","Mark = 90")

T("2. Object-Oriented Programming Paradigms")
P("OOP organizes a program around <b>objects and their interactions</b>.")
P("<b>Main concepts:</b> Classes, Objects, Encapsulation, Abstraction, Inheritance, Polymorphism and Message Passing.")
K("OOP improves code reusability, modularity, security and maintainability.")
C("""class ClassName {
    dataType variable;

    returnType methodName() {
        // statements
    }
}""")

T("3. Features of OOP")
P("<b>Encapsulation:</b> Binding data and methods into one unit.")
C("""class Student {
    private int mark;

    public void setMark(int m) {
        mark = m;
    }

    public int getMark() {
        return mark;
    }
}""")
P("<b>Abstraction:</b> Hiding implementation details.")
C("""abstract class Shape {
    abstract void draw();
}""")
P("<b>Inheritance:</b> Acquiring properties and methods from another class.")
C("""class Child extends Parent {
}""")
P("<b>Polymorphism:</b> One interface/name can represent different forms.")
C("""Parent obj = new Child();
obj.show();""")
K("The four major OOP features are Encapsulation, Abstraction, Inheritance and Polymorphism.")

T("4. Java Buzzwords")
P("Important Java characteristics are <b>Simple, Object-Oriented, Distributed, Robust, Secure, Architecture Neutral, Portable, High Performance, Multithreaded and Dynamic</b>.")
K("Java supports Write Once, Run Anywhere (WORA) through bytecode and JVM.")
C("""Source Code
    ↓
Compiler
    ↓
Bytecode
    ↓
JVM
    ↓
Output""")

T("5. Overview of Java")
P("<b>Definition:</b> Java is a high-level, object-oriented programming language.")
C("""class ClassName {
    public static void main(String[] args) {
        // statements
    }
}""")
program("Basic Java","""class Hello {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}""","Hello Java")

T("6. Data Types, Variables and Arrays")
P("<b>Primitive data types:</b> byte, short, int, long, float, double, char and boolean.")
P("<b>Variable:</b> A named memory location used to store a value.")
C("""dataType variableName = value;""")
P("<b>Array:</b> A fixed-size collection of elements of the same type.")
C("""dataType[] arrayName = new dataType[size];

int[] a = {10, 20, 30};

arrayName[index];""")
program("Array","""class ArrayDemo {
    public static void main(String[] args) {
        int[] a = {10, 20, 30};

        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}""","10\n20\n30")

T("7. Operators")
P("<b>Arithmetic:</b> +, -, *, /, %<br/><b>Relational:</b> ==, !=, &gt;, &lt;, &gt;=, &lt;=<br/><b>Logical:</b> &amp;&amp;, ||, !<br/><b>Assignment:</b> =, +=, -=, *=, /=<br/><b>Unary:</b> ++, --<br/><b>Conditional:</b> ?:")
program("Operators","""class OperatorDemo {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        System.out.println(a + b);
        System.out.println(a > b);
        System.out.println(a % b);
    }
}""","13\ntrue\n1")

T("8. Control Statements")
P("<b>Selection:</b> if, if-else, switch. <b>Iteration:</b> for, while, do-while. <b>Jump:</b> break, continue, return.")
C("""if (condition) {
    // statements
}

for (initialization; condition; update) {
    // statements
}

while (condition) {
    // statements
}

do {
    // statements
} while (condition);""")
program("Control Statements","""class ControlDemo {
    public static void main(String[] args) {
        int n = 5;

        if (n % 2 == 0)
            System.out.println("Even");
        else
            System.out.println("Odd");

        for (int i = 1; i <= 3; i++)
            System.out.println(i);
    }
}""","Odd\n1\n2\n3")

T("9. Programming Structures in Java")
P("The three basic programming structures are <b>Sequence, Selection and Iteration</b>.")
C("""// Sequence
statement1;
statement2;
statement3;

// Selection
if (condition) {
    // statements
}

// Iteration
for (initialization; condition; update) {
    // statements
}""")
K("Sequence executes in order; selection chooses a path; iteration repeats statements.")

T("10. Defining Classes in Java")
P("A class is a blueprint for creating objects.")
C("""class ClassName {
    dataType variable;

    returnType methodName() {
        // statements
    }
}

ClassName objectName = new ClassName();""")
program("Class and Object","""class Student {
    int id;
    String name;

    void display() {
        System.out.println(id + " " + name);
    }

    public static void main(String[] args) {
        Student s = new Student();
        s.id = 101;
        s.name = "Arun";
        s.display();
    }
}""","101 Arun")

T("11. Constructors")
P("A constructor initializes an object. It has the <b>same name as the class</b> and has <b>no return type</b>.")
C("""class ClassName {
    ClassName() {
        // initialization
    }

    ClassName(dataType value) {
        // initialization
    }
}""")
program("Parameterized Constructor","""class Student {
    int id;
    String name;

    Student(int i, String n) {
        id = i;
        name = n;
    }

    void display() {
        System.out.println(id + " " + name);
    }

    public static void main(String[] args) {
        Student s = new Student(101, "Arun");
        s.display();
    }
}""","101 Arun")

T("12. Methods")
P("A method is a named block of code that performs a specific task.")
C("""returnType methodName() {
    // statements
}

returnType methodName(dataType parameter) {
    // statements
}

returnType methodName() {
    return value;
}""")
program("Method","""class MethodDemo {
    static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(add(10, 20));
    }
}""","30")

T("13. Access Specifiers")
P("Access specifiers control the visibility of class members.")
C("""private int x;
int x;              // default
protected int x;
public int x;""")
K("private → same class; default → same package; protected → package + subclass access; public → broadly accessible.")

T("14. Static Members")
P("A static member belongs to the <b>class</b> rather than an individual object.")
C("""static dataType variableName;

static returnType methodName() {
    // statements
}

ClassName.variableName;
ClassName.methodName();""")
program("Static Member","""class Counter {
    static int count = 0;

    Counter() {
        count++;
    }

    public static void main(String[] args) {
        new Counter();
        new Counter();
        System.out.println(count);
    }
}""","2")

T("15. JavaDoc Comments")
P("JavaDoc comments are documentation comments used to describe Java code and generate documentation.")
C("""/**
 * Description
 * @param parameter Description
 * @return Description
 */""")
K("Common tags: @param, @return, @author and @throws.")

story.append(PageBreak())

# UNIT II
P("UNIT II — INHERITANCE, PACKAGES AND INTERFACES","Unit")

T("16. Overloading Methods")
P("Method overloading means having the <b>same method name with different parameter lists</b>. It is compile-time polymorphism.")
C("""class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}""")
program("Method Overloading","""class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.println(c.add(2, 3));
        System.out.println(c.add(2, 3, 4));
    }
}""","5\n9")
K("Same name + different parameters = Overloading. Return type alone cannot overload a method.")

T("17. Objects as Parameters")
P("An object can be passed as an argument to a method.")
C("""returnType methodName(ClassName object) {
    // statements
}

methodName(object);""")
program("Object as Parameter","""class Student {
    int mark;

    Student(int m) {
        mark = m;
    }

    static void display(Student s) {
        System.out.println("Mark = " + s.mark);
    }

    public static void main(String[] args) {
        Student s = new Student(90);
        display(s);
    }
}""","Mark = 90")

T("18. Returning Objects")
P("A method can return an object of a class.")
C("""ClassName methodName() {
    return object;
}

ClassName obj = methodName();""")
program("Returning Object","""class Number {
    int value;

    Number(int v) {
        value = v;
    }

    static Number create() {
        return new Number(50);
    }

    public static void main(String[] args) {
        Number n = create();
        System.out.println(n.value);
    }
}""","50")

T("19. Static, Nested and Inner Classes")
P("A nested class is declared inside another class. A static nested class is declared using static. A non-static nested class is an inner class.")
C("""class Outer {
    static class Nested {
        // members
    }

    class Inner {
        // members
    }
}

Outer.Nested n = new Outer.Nested();

Outer o = new Outer();
Outer.Inner i = o.new Inner();""")
program("Nested and Inner Classes","""class Outer {
    static class Nested {
        void show() {
            System.out.println("Nested Class");
        }
    }

    class Inner {
        void show() {
            System.out.println("Inner Class");
        }
    }

    public static void main(String[] args) {
        Nested n = new Nested();
        n.show();

        Outer o = new Outer();
        Inner i = o.new Inner();
        i.show();
    }
}""","Nested Class\nInner Class")

T("20. Inheritance — Basics and Types")
P("Inheritance allows a child class to acquire properties and methods from a parent class.")
C("""class Parent {
    // members
}

class Child extends Parent {
    // members
}""")
P("<b>Types:</b> Single, Multilevel and Hierarchical inheritance. Java does not support multiple inheritance through classes.")
program("Inheritance","""class Animal {
    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }

    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.bark();
    }
}""","Eating\nBarking")

T("21. super Keyword")
P("The super keyword refers to the <b>immediate parent class</b>.")
C("""super.variableName;
super.methodName();
super();""")
program("super Keyword","""class Parent {
    int x = 10;

    void show() {
        System.out.println("Parent Method");
    }
}

class Child extends Parent {
    int x = 20;

    void display() {
        System.out.println(super.x);
        super.show();
    }

    public static void main(String[] args) {
        Child c = new Child();
        c.display();
    }
}""","10\nParent Method")

T("22. Method Overriding")
P("Method overriding occurs when a subclass provides its own implementation of an inherited method with the same signature.")
C("""class Parent {
    void show() {
        // parent implementation
    }
}

class Child extends Parent {
    @Override
    void show() {
        // child implementation
    }
}""")
program("Method Overriding","""class Animal {
    void sound() {
        System.out.println("Animal Sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog Sound");
    }

    public static void main(String[] args) {
        Dog d = new Dog();
        d.sound();
    }
}""","Dog Sound")

T("23. Dynamic Method Dispatch")
P("Dynamic method dispatch selects an overridden method at <b>runtime</b>.")
C("""Parent reference = new Child();
reference.method();""")
program("Dynamic Method Dispatch","""class Animal {
    void sound() {
        System.out.println("Animal");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog");
    }

    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
    }
}""","Dog")
K("Parent reference + child object + overridden method = runtime method selection.")

T("24. Abstract Classes")
P("An abstract class is declared using the abstract keyword. It may contain abstract and concrete methods and cannot be instantiated directly.")
C("""abstract class Shape {
    abstract void draw();

    void message() {
        // statements
    }
}

class Circle extends Shape {
    void draw() {
        // implementation
    }
}""")
program("Abstract Class","""abstract class Shape {
    abstract void draw();

    void message() {
        System.out.println("Shape");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Circle");
    }

    public static void main(String[] args) {
        Circle c = new Circle();
        c.draw();
        c.message();
    }
}""","Circle\nShape")

T("25. final with Inheritance")
P("final is used to restrict modification or inheritance.")
C("""final int x = 10;       // cannot reassign

final void show() {     // cannot override
}

final class A {         // cannot extend
}""")
K("final variable → cannot reassign; final method → cannot override; final class → cannot extend.")

T("26. Packages and Member Access")
P("A package is a group of related classes and interfaces. Packages organize code, avoid naming conflicts and provide access control.")
C("""package packageName;

class Student {
}""")
K("Access modifiers work with packages: private, default, protected and public.")

T("27. Importing Packages")
P("The import statement allows a program to use classes from another package.")
C("""import packageName.ClassName;

import java.util.*;
import java.util.Scanner;""")
program("Importing a Package","""import java.util.ArrayList;

class ImportDemo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();

        list.add("Java");
        list.add("OOP");

        System.out.println(list);
    }
}""","[Java, OOP]")

T("28. Interfaces")
P("An interface defines a contract that a class implements.")
C("""interface InterfaceName {
    void methodName();
}

class ClassName implements InterfaceName {
    public void methodName() {
        // implementation
    }
}

class Demo implements Interface1, Interface2 {
}""")
program("Interface","""interface Printable {
    void print();
}

class Demo implements Printable {
    public void print() {
        System.out.println("Printing");
    }

    public static void main(String[] args) {
        Demo d = new Demo();
        d.print();
    }
}""","Printing")

story.append(PageBreak())

# UNIT III
P("UNIT III — EXCEPTION HANDLING AND MULTITHREADING","Unit")
P("The uploaded syllabus image is cropped after the beginning of “Java Thread Model”. The notes below therefore cover only the visible Unit III topics and do not guess the missing topics.","NoteX")

T("29. Exception Handling")
P("An exception is an abnormal event that interrupts the normal flow of program execution.")
C("""try {
    // risky code
}
catch (ExceptionType e) {
    // handling code
}
finally {
    // cleanup
}""")
program("Exception Handling","""class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int x = 10 / 0;
            System.out.println(x);
        }
        catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        }
    }
}""","Cannot divide by zero")
K("try = risky code; catch = handling; finally = cleanup.")

T("30. Multiple Catch Clauses")
P("Multiple catch blocks handle different types of exceptions from one try block.")
C("""try {
    // statements
}
catch (ExceptionType1 e) {
    // handling
}
catch (ExceptionType2 e) {
    // handling
}
catch (Exception e) {
    // handling
}""")
program("Multiple Catch","""class MultiCatchDemo {
    public static void main(String[] args) {
        try {
            int[] a = {10, 20};
            System.out.println(a[5]);
        }
        catch (ArithmeticException e) {
            System.out.println("Arithmetic Error");
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index Error");
        }
        catch (Exception e) {
            System.out.println("Other Error");
        }
    }
}""","Array Index Error")

T("31. Nested try Statements")
P("A try block placed inside another try block is called a nested try.")
C("""try {
    // outer code

    try {
        // inner code
    }
    catch (ExceptionType e) {
        // inner handling
    }

}
catch (ExceptionType e) {
    // outer handling
}""")
program("Nested try","""class NestedTryDemo {
    public static void main(String[] args) {
        try {
            System.out.println("Outer Try");

            try {
                int x = 10 / 0;
            }
            catch (ArithmeticException e) {
                System.out.println("Inner Catch");
            }

        }
        catch (Exception e) {
            System.out.println("Outer Catch");
        }
    }
}""","Outer Try\nInner Catch")

T("32. Java's Built-in Exceptions")
P("Java provides predefined exception classes for common errors.")
P("<b>Examples:</b> ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException and ClassCastException.")
C("""try {
    // code
}
catch (ExceptionType e) {
    // handling
}""")
program("Built-in Exception","""class BuiltInDemo {
    public static void main(String[] args) {
        try {
            int n = Integer.parseInt("ABC");
            System.out.println(n);
        }
        catch (NumberFormatException e) {
            System.out.println("Invalid Number");
        }
    }
}""","Invalid Number")

T("33. User-defined Exceptions")
P("A user-defined exception is a custom exception created by the programmer, commonly by extending Exception.")
C("""class MyException extends Exception {
    MyException(String message) {
        super(message);
    }
}

throw new MyException("Error");

void check() throws MyException {
    // statements
}

try {
    check();
}
catch (MyException e) {
    System.out.println(e.getMessage());
}""")
program("User-defined Exception","""class AgeException extends Exception {
    AgeException(String message) {
        super(message);
    }
}

class UserExceptionDemo {
    static void checkAge(int age) throws AgeException {
        if (age < 18)
            throw new AgeException("Age is below 18");

        System.out.println("Eligible");
    }

    public static void main(String[] args) {
        try {
            checkAge(16);
        }
        catch (AgeException e) {
            System.out.println(e.getMessage());
        }
    }
}""","Age is below 18")

T("34. Multithreaded Programming")
P("Multithreading means executing multiple threads within a program. A thread is a lightweight unit of execution.")
P("<b>Two common approaches:</b> extending Thread and implementing Runnable.")
C("""class MyThread extends Thread {
    public void run() {
        // thread task
    }
}

MyThread t = new MyThread();
t.start();""")
program("Thread Class","""class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}

class ThreadDemo {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}""","Thread is running")

C("""class MyTask implements Runnable {
    public void run() {
        // task
    }
}

MyTask task = new MyTask();
Thread t = new Thread(task);
t.start();""")
program("Runnable","""class Task implements Runnable {
    public void run() {
        System.out.println("Task is running");
    }
}

class RunnableDemo {
    public static void main(String[] args) {
        Thread t = new Thread(new Task());
        t.start();
    }
}""","Task is running")

T("35. Java Thread Model")
P("The Java Thread Model provides a standard mechanism for creating and managing threads.")
C("""Create Thread
     ↓
   start()
     ↓
Thread begins execution
     ↓
   run()
     ↓
Task completed""")
P("<b>Important methods:</b>")
C("""t.start();          // starts a new thread
t.run();            // contains thread task
Thread.sleep(1000); // pauses current thread
t.join();           // waits for thread to finish""")
program("Java Thread Model","""class MyThread extends Thread {
    public void run() {
        System.out.println("Running Thread");
    }

    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}""","Running Thread")

story.append(PageBreak())

# Revision
P("QUICK REVISION — IMPORTANT SYNTAX","Unit")
P("<b>Class and Object</b>","Topic")
C("""class A { }

A obj = new A();""")
P("<b>Constructor and Method</b>","Topic")
C("""A() { }

void show() {
}""")
P("<b>Overloading and Overriding</b>","Topic")
C("""// Overloading
void add(int a) { }
void add(int a, int b) { }

// Overriding
@Override
void show() { }""")
P("<b>Inheritance and super</b>","Topic")
C("""class B extends A {
}

super.x;
super.show();
super();""")
P("<b>Abstract and final</b>","Topic")
C("""abstract class A {
    abstract void show();
}

final int x = 10;
final void show() { }
final class A { }""")
P("<b>Package and Interface</b>","Topic")
C("""package mypack;

import java.util.*;

interface A {
    void show();
}

class B implements A {
    public void show() { }
}""")
P("<b>Exception Handling</b>","Topic")
C("""try {
    // risky code
}
catch (Exception e) {
    // handling
}
finally {
    // cleanup
}

throw new MyException("Error");

void check() throws Exception {
}""")
P("<b>Thread</b>","Topic")
C("""class T extends Thread {
    public void run() {
        // task
    }
}

T t = new T();
t.start();""")

P("MOST IMPORTANT DIFFERENCES","Unit")
C("""Overloading  → same name + different parameters
Overriding    → same method + child implementation
Inheritance   → child acquires parent members
Abstraction   → hides implementation details
Encapsulation  → binds data + methods
Polymorphism   → one name/interface, different forms
final variable → cannot reassign
final method   → cannot override
final class    → cannot extend""")

P("END OF NOTES","Cover")
P("Definitions + Explanation + Key Points + Syntax + Programs + Outputs","NoteX")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(HexColor("#D9E2F3"))
    canvas.line(15*mm,10*mm,A4[0]-15*mm,10*mm)
    canvas.setFont("Helvetica",7.5)
    canvas.setFillColor(HexColor("#666666"))
    canvas.drawString(15*mm,5.5*mm,"Java Programming — Complete Exam Notes")
    canvas.drawRightString(A4[0]-15*mm,5.5*mm,f"Page {doc.page}")
    canvas.restoreState()

doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)


    