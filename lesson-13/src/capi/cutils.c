#include <stdlib.h>
#include <stdio.h>

#include <Python.h>

int rfib(int n)
{
    if (n < 2)
        return 1;
    return rfib(n-2) + rfib(n-1);
}

PyObject* cutils_rfib(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("Failed to parse arguments");
        return NULL;
    }

    int res = rfib(n);
    return Py_BuildValue("i", res);
    //return PyLong_FromLong(res);
}

PyObject* cutils_fib(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("Failed to parse arguments");
        return NULL;
    }
    int a = 1, b = 1;
    for (int i = 0; i < n; ++i)
    {
        int tmp = a;
        a = a+b;
        b = tmp;
    }
    int res = b;
    return Py_BuildValue("i", res);
    //return PyLong_FromLong(res);
}

static PyMethodDef methods[] = {
    {"rfib", cutils_rfib, METH_VARARGS, "Recursive version of fibonacci."},
    {"fib", cutils_fib, METH_VARARGS, "Iterative version of fibonacci."},
    {NULL, NULL, NULL, NULL}
};

static PyModuleDef module_def = {
    PyModuleDef_HEAD_INIT,
    "cutils",
    "Some useful module.",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_cutils(void) {
    return PyModule_Create(&module_def);
}
