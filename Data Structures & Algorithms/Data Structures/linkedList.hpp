#include <iostream>
using namespace std;

#ifndef LINKEDLIST 
#define LINKEDLIST


typedef struct linkedNode{
    int number;
    struct linkedNode *next;
}
linkedNode;

class LinkedList{
    public:
    linkedNode *list;
    int len;
    explicit LinkedList(){
        this->list = NULL;
        this->len = 0;
    }
    // Converts an array to a linked list
    linkedNode* conv(int arr[],int length){
        for (int i = 0; i < length; i++){
            append(arr[i]);
        }
        return this->list;
    }
    // Finds the addr for the second last pointer of the given index on the linked list
    linkedNode* find(int index=-1,int num=0){
        int curr = 0;
        for (linkedNode *temp = this->list; temp != NULL; temp = temp->next){
        // If number exists then search for the place where the number is lower than temp but higher than the next num
        if (num){   
             if (num > temp->number && num < temp->next->number ){
                return temp;
            }
        }
        else{
            if (index >= 0){
                if (index == 0){    // Return if it's the first one
                    return temp;
                }
                else if (curr + 1 == index){    // Have to check against the actual index so +1
                    return temp;
                }
                curr++;
            }
            else{
                if (temp-> next == NULL){   // Finds the last index
                    return temp;
                }
            }
         }
        }
        return NULL;
    }

    // Inserts into a certain index or in an ascending form
    void insert(int num,int index=0,bool sorted=false){
        linkedNode *n = createNode(num);
        if (!sorted){
            linkedNode *temp = find(index);
            if (index == 0){    // Insert into first index
                if (this->len == 0){
                    list = n;
                    this->len++;
                    return;
                }
                n->next = temp->next;   // Connecting
                this->list = n;
                return;
            }
            n->next = temp->next->next;
            temp->next = n;
            return;
        }
        linkedNode *temp = find(-1,2);
        n->next = temp->next;   // Insert
        temp->next = n;
    }

    // Removes the number of the given index from the linked list
    void remove(int index){
        linkedNode *n = find(index);
        linkedNode *temp = NULL;
        if (index == 0){    // Removes first index
            temp = this->list->next;
            free(this->list);
            this->list = temp;
            return;
        }
        temp = n->next->next;
        free(n->next);
        n->next = temp;        
        this->len--;
    }

    // Creates a node of that number
    linkedNode *createNode(int num){
        linkedNode *n = NULL;
        n = (struct linkedNode*)malloc(sizeof(linkedNode));
        n->number = num;
        n->next = NULL;
        return n;
    }

    // Appends a number to the last of the linked list
    void append(int num){
        linkedNode *last = NULL;
        linkedNode *n = createNode(num);
        if (this->len == 0){
            this->list = n;
            this->len ++;
            return;
        }
        last = find();
        last->next = n;
        this->len++;
    }
    // Prints either a specific index of the list or the entire list
    void print(int index =-1){
        if (index >= 0){
            linkedNode *res = find(index);
            if (index == 0){
                cout << res->number << '\n';
                return;
            }
            cout << res->next->number << '\n';
            return;
        }
        for (linkedNode *temp = this->list; temp != NULL; temp = temp->next){
            cout << temp->number << '\n';
        }
    }

    // Frees all the nodes in the linked list
    void freeAll(){
        linkedNode *temp = NULL;
        for (linkedNode *temp2 = this->list; temp2 != NULL; temp2 = temp){
            temp = temp2->next;
            free(temp2);
        }
    }
};

#endif