#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a
 * cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *l2;
	listint_t *pre;

	l2 = list;
	pre = list;
	while (list && l2 && l2->next)
	{
		list = list->next;
		l2 = l2->next->next;

		if (list == l2)
		{
			list = pre;
			pre = l2;
			while (1)
			{
				l2 = pre;
				while (l2->next != list && l2->next != pre)
				{
					l2 = l2->next;
				}
				if (l2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
