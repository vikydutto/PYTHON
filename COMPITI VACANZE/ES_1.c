#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int num;
    struct node*nextptr;
}Stnode;


/*void createNodeList(int n);
void lastNodeDeletetion();
void displayList();*/


void createNodeList(n){
    struct node* fnNode, *tmp;
    int num;
    int i;

    Stnode = (struct node*)malloc(sizeof(struct node));
    if(Stnode = NULL){
        printf("La memoria non può essere allocata");
    }else{
        printf("Inserisci il nodo 1: ");
        scanf("%d", &num);
    }
}


int main(){
    int n;//numero nodi
    int num;
    int pos;

    printf("Inserisci il numero dei nodi: ");
    scanf("%d", &n);

    createNodeList(n);
    printf("\n I numeri della lista inseriti sono: \n");
    displayList();
    return 0;

}

