#include <stdio.h>
#include <stdlib.h>


typedef struct NodeStruct
{
    struct NodeStruct *previous;
    struct NodeStruct *next;
    int value;
} Node_t;


typedef struct HeadAndTailStruct
{
    Node_t *head;
    Node_t *tail;
} HeadAndTail_t;


void addNewNode(int value, HeadAndTail_t *headAndTail)
{
    if(headAndTail -> head == NULL)
    {
        Node_t *node = malloc(sizeof(Node_t));
        node->previous = NULL;
        node->next = NULL;
        node->value = value;
        headAndTail->head = node;
        headAndTail->tail = node;
    }
    else
    {
        Node_t *node = malloc(sizeof(Node_t));
        node->previous = headAndTail->tail;
        node->next = NULL;
        node->value = value;
        headAndTail->tail->next = node;
        headAndTail->tail = node;
    }
}


void printNode(Node_t *node)
{
    printf("%d", node->value);
}


void printLinkedList(HeadAndTail_t *headAndTail)
{
    Node_t *currentNode = headAndTail->head;
    while(currentNode != NULL)
    {
        printNode(currentNode);
        if(currentNode->next != NULL) printf(" - ");
        currentNode = currentNode->next;
    }
    printf("\n");
}


void deleteNode(int value, HeadAndTail_t *headAndTail)
{
    Node_t *currentNode = headAndTail->head;
    while(currentNode != NULL)
    {
        if(currentNode->value == value)
        {
            if(currentNode->previous != NULL) currentNode->previous->next = currentNode->next;
            if(currentNode->previous == NULL) headAndTail->head = currentNode->next;
            if(currentNode->next != NULL) currentNode->next->previous = currentNode->previous;
            if(currentNode->next == NULL) headAndTail->tail = currentNode->previous;
            free(currentNode);
            return;
        }

        currentNode = currentNode->next;
    }
}


void insertNewNode(int value, int position, HeadAndTail_t *headAndTail)
{
    if(position == 0)
    {
        Node_t *node = malloc(sizeof(Node_t));
        node->next = headAndTail->head;
        node->previous = NULL;
        node->value = value;
        node->next->previous = node;
        headAndTail->head = node;
        return;
    }

    Node_t *currentNode = headAndTail->head;
    int counter = 0;
    while(currentNode != NULL)
    {
        if(counter == position)
        {
            Node_t *node = malloc(sizeof(Node_t));
            node->next = currentNode;
            node->previous = currentNode->previous;
            node->value = value;
            currentNode->previous->next = node;
            currentNode->previous = node;
            return;
        }

        if(currentNode->next == NULL)
        {
            addNewNode(value, headAndTail);
            return;
        }

        ++counter;
        currentNode = currentNode->next;
    }
}


int main()
{
    HeadAndTail_t headAndTail = {NULL, NULL};

    for(int i = 1; i <= 10; i++)
    {
        addNewNode(i, &headAndTail);
    }

    addNewNode(11, &headAndTail);
    deleteNode(8, &headAndTail);
    deleteNode(1, &headAndTail);
    insertNewNode(99, 2, &headAndTail);
    insertNewNode(1, 0, &headAndTail);
    insertNewNode(99, 1000, &headAndTail);
    printLinkedList(&headAndTail);

    return 0;
}