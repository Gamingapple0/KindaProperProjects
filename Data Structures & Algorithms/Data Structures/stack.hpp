#include <iostream>
#include "linkedList.hpp"
using namespace std;

#ifndef STACK
#define STACK

class Stack:public LinkedList{
    public:
    void push(int num){
        append(num);
    }

    int pop(){
        linkedNode *temp = find(this->len - 1);
        int num = temp->next->number;
        free(temp->next);
        temp->next = NULL;
        return num;
    }
};


#endif