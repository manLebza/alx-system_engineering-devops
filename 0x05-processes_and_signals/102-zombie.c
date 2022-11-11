#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while -> function contains an infinite loop
 * Return: always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main -> entry point
 * Return: always 0
 */

int main(void)
{
	int x;

	for (x = 0; x < 5; x++)
	{
		if (fork() == 0)
		{
			dprint(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}

	infinite_while();

	return (0);
}
