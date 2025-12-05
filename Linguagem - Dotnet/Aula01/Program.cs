// using static System.Console;

// WriteLine("Digite Algo... ");
// string texto = ReadLine();

// BackgroundColor = ConsoleColor.White;
// ForegroundColor = ConsoleColor.Blue;

// CursorVisible = false;

// Clear();

// Write("O usuario digitou: ");
// ForegroundColor = ConsoleColor.Red;
// Write(texto);



int a = 1;
int b = 1;

Console.WriteLine(a);
Console.WriteLine(b);

b = a++;
System.Console.WriteLine($"A:{a} | B:{b}");
b = a++;
System.Console.WriteLine($"A:{a} | B:{b}");
b = a++;
System.Console.WriteLine($"A:{a} | B:{b}");

a = 1;
b = 1;

Console.WriteLine(a);
Console.WriteLine(b);

b = ++a;
System.Console.WriteLine($"A:{a} | B:{b}");
b = ++a;
System.Console.WriteLine($"A:{a} | B:{b}");
b = ++a;
System.Console.WriteLine($"A:{a} | B:{b}");