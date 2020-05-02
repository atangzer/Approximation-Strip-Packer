#include <stdio.h>
#include <stdlib.h>

struct minheap_struct{  //min_heap structure is used to implement heap sort
    int *nodes; //stores the nodes in the min_heap. the 0th element in the array should be a sentinel node
    int size;   //stores the number of nodes in the heap
    int capacity;   //stores the maximum number of nodes the heap can store, based on the memory allocated
};

typedef struct minheap_struct *minheap;

minheap buildheap(int n, int* heights); //O(N) algorithm to build a heap from the input, returns a heap
int pop(minheap h, int* heights);   //removes the top item from the heap h, maintains the heap structure, and returns the removed item
int* sort(minheap h, int* heights); //iterativey pops items from the heap h until it is empty, returns an array containing the items in decreasing order of their heights
int isEmpty(minheap h); //checks if the heap h is empty. returns 1 if true, 0 if false

int main(){
    int texture_width, num_images;
    scanf("%d %d", &texture_width, &num_images);

    int *lvls=(int*)calloc(sizeof(int), num_images);
    int *next=(int*)calloc(sizeof(int), num_images+1);
    int *used=(int*)calloc(sizeof(int), num_images);

    int* heights=(int*)malloc(sizeof(int)*num_images);
    int* widths=(int*)malloc(sizeof(int)*num_images);

    for(int i=0;i<num_images;i++){
        scanf("%d %d", heights+i, widths+i);
        if(heights[i]<1 || heights[i]>texture_width){
            printf("Invalid Input\n");
            return 1;
        }
    }

    minheap h=buildheap(num_images, heights);
    int* sorted=sort(h, heights);

    free(h);

    for(int i=0;i<num_images;i++)   printf("%d ", heights[sorted[i]]);
    printf("\n");

    return 0;
}

int* sort(minheap h, int* heights){     //takes as arguements a minheap h and an array containing the heights of the images  
    while(!isEmpty(h))  pop(h, heights);    //pops elements until there are none left
    return h->nodes+1;  //when the heap is empty, the array of elements in the heap will be in decreasing order. the 0th node is a sentinel. therefore, we return h->nodes[1:]
}

minheap buildheap(int n, int* heights){ //takes as arguements the number of images and an array containing the heights of the images
    minheap h=(minheap)malloc(sizeof(struct minheap_struct));   //allocates memory for the minheap structure
    h->capacity=n;  //sets the max capacity and size of the structure to be equal to the size of the structure
    h->size=n;
    h->nodes=(int*)malloc(sizeof(int)*(n+1));   //allocates memory for the nodes of the minheap
    h->nodes[0]=-1; //assigns the value -1 to the sentinel node at position 0
    h->nodes[1]=0;  //assigns the address of the 0th image to the root of the minheap, adding the first node to the minheap

    int j, minchild;    //j is an iterator used to travel down the tree while "percolating down". minchild stores the minimum child of node while percolating down
    for(int i=h->size;i>0;i--){
        j=i;    //start at the next empty position in the tree
        while(2*j < h->size){   //while the current node has children
            minchild=2*j;   //assume the left child has smallest height
            if(minchild+1<h->size && heights[h->nodes[minchild]] > heights[h->nodes[minchild+1]])     minchild++;   //if the height of the right child is smaller, update minchild
            if(heights[i-1] > heights[h->nodes[minchild]]){     //if the height of the node to be inserted is less than the smallest of the heights of its children
                h->nodes[j]=h->nodes[minchild]; //percolate the child up
                j=minchild; //move down a level
            }
            else    break;  //the current node has smaller height than both of its children
        }
        h->nodes[j]=i-1;    //insert the new node at the position found
    }   // !!!NOTE!!! that the values that are stored in the min heap are not the heights of the images, but rather the addresses of each image in the heights and widths arrays. The nodes are sorted however according to their heights.
    return h;   //return the built heap
}

int pop(minheap h, int* heights){   //takes as arguements a heap h to be popped from and the array of image heights which is needed to maintain the heap order
    
    int temp=h->nodes[h->size]; //saves the last item in the heap
    h->nodes[h->size]=h->nodes[1];  //moves the item at the top of the heap to the former last position in the array which will now be outside of the heap
    h->size--;  //decreases the heap size, excluding the last position in the array from the heap

    int i=1, minchild;  //i is an iterator used to travel down the heap while percolating down, minchild is used to store the child of the current node with smallest height
    //i is set to the top node in the heap
    while(i*2<h->size+1){   //while the current node has children
        minchild=i*2;   //assume the left child has smallest height
        if(minchild<h->size && heights[h->nodes[minchild]]>heights[h->nodes[minchild+1]])     minchild++;   //if the height of the right child is smaller, update minchild
        if(heights[temp]>heights[h->nodes[minchild]]){      //if the former last node in the array has greater height than both children of the current node
            h->nodes[i]=h->nodes[minchild]; //percolate the child with minimum height up
            i=minchild; //move down a level
        }
        else break;     //the current child has no children
    }
    h->nodes[i]=temp;   //insert the former last node at the position found
    return h->nodes[h->size+1];     //return the former top node
}

int isEmpty(minheap h){     //takes a min heap as an arguement
    if(h->size==0)  return 1;   //empty
    else return 0;  //not empty
}