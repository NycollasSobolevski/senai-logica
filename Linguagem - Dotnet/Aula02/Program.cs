// int idade = 19;

// switch (idade)
// {
//     case 18:
//         System.Console.WriteLine("Agora é maior de idade");
//         break;
//     case 19:

//         System.Console.WriteLine("Tá ficando veio");
//         goto case 18;

// }



// Exemplo for:

// for (int i = 2; i < 10; i += 2)
// {
//     System.Console.WriteLine(i);
// }


// Exemplo funções 

// calculo de módulo:

int valor = Modulo(-3);
System.Console.WriteLine(valor);

int Modulo(int numero)  
{
    if (numero < 0)
    {
        numero = -numero;
    }
    return numero;
}