#include <iostream>
#include "linkedList.hpp"
using namespace std;

#ifndef QUEUE
#define QUEUE

class Queue:public LinkedList{
    public:

    // Adds the number to the back of the queue
    void enqueue(int num){
        append(num);
    }

    // Removes and returns the first 
    int dequeue(){
        int res = this->list->number ;
        linkedNode *temp = this->list->next;
        free(this->list);
        this->list = temp;
        this->len--;
        return res;
    }
};

#endif
