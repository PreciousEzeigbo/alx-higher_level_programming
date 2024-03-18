#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int i = 0, list_l = 0;
    PyObject *item;
    PyListObject *clone = (PyListObject *) p;

    list_l = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", list_l);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; i < list_l; ++i)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
    }

    return;
}
