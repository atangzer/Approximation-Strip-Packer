#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//algorithm adapted from the nfdh algorithm described at: https://cgi.csc.liv.ac.uk/~epa/surveyhtml.html#bib.1

struct minheap_struct{  //min_heap structure is used to implement heap sort
    int *nodes; //stores the nodes in the min_heap. the 0th element in the array should be a sentinel node
    int size;   //stores the number of nodes in the heap
    int capacity;   //stores the maximum number of nodes the heap can store, based on the memory allocated
};

typedef struct minheap_struct *minheap;

int texture_width, num_images;  //texture_width stores the given width of the texture atlas. num_images stores the number of images to be packed
int *image_height, *image_width, *x_pos, *y_pos;    //image_height and image_width store the heights and widths of the images, respectively
                                                    //x_pos and y_pos store the x and y coordinates, respectively, of the bottom left pixel in the image

minheap buildheap(); //O(N) algorithm to build a min heap from the images according to their heights, returns a heap
int pop(minheap h);   //removes the top item from the heap h, maintains the heap structure, and returns the removed item
int* sort(minheap h); //iterativey pops items from the heap h until it is empty, returns an array containing the items in decreasing order of their heights
int isEmpty(minheap h); //checks if the heap h is empty. returns 1 if true, 0 if false

int nfdhPack(int* images);   //packs images in the order given by the parameter images. writes the position of images in the NFDH packing to x_pos, y_pos, returns the height of the packing

int main(){
    printf("Input:\n");
    scanf("%d %d", &texture_width, &num_images);

    clock_t begin = clock(); //Time at beginning (after the scanf)

    image_height=(int*)malloc(sizeof(int)*num_images);  //stores the heights of image
    image_width=(int*)malloc(sizeof(int)*num_images);   //stores the widths of the image

    x_pos=(int*)malloc(sizeof(int)*num_images);    //stores the x_pos of the bottom left pixel of each image
    y_pos=(int*)malloc(sizeof(int)*num_images);    //stores the y_pos of the bottom left pixel of each image

    int error_flag=0;
    for(int i=0;i<num_images;i++){  //for all i images
        scanf("%d %d", image_width+i, image_height+i);    //read in the height and width of the image
        if(image_width[i]<1 || image_height[i]<1 || image_width[i]>texture_width){   //if the image has negative or zero dimensions or if the image is wider than the texture atlas
            error_flag=1;   //catch the error
        }
    }

    if(error_flag){ //an error was caught
        printf("Invalid Input\n");
        return 1;   //end the program because the input is invalid, return 1 to flag error
    }

    minheap h=buildheap();   //builds a min heap of the images
    int* sortedImages=sort(h);   //sorts the images in decreasing order of their heights and stores them in the int array sorted

    free(h);    //deallocates h as it is no longer needed

    int area=texture_width*nfdhPack(sortedImages);  //calls the 2d packing algorithm

    printf("\nOutput:\n");
    printf("area=%d\n",area);
    for(int i=0;i<num_images;i++)   printf("(%d, %d)\n", x_pos[i], y_pos[i]);   //output the (x,y) coordinates of the images in the texture atlas

    clock_t end = clock(); //Time at end
    double elapsed_time = ((double)(end - begin) / CLOCKS_PER_SEC) * 1000000000; //Time taken = time at beginning - time at end; Multiply by 10^9 to get nanoseconds
    printf("\nTime taken by program was %f nanoseconds\n", elapsed_time);

    return 0;   //end of program, return 1, no errors
}

int nfdhPack(int* images){
    int* lvl_height=(int*)calloc(sizeof(int), num_images);    //stores the height of each level. an empty level has height 0
    int* used_width=(int*)calloc(sizeof(int), num_images);    //stores the width of space already occupied in each level. and empty level has 0 width.

    int current_lvl=0;  //used as pointer to the top level
    int current_image=images[0];    //used as pointer to the current image. initialized as image with greatest height
    int current_y=0;    //used to set the y coordinates of images, initialized to 0

    x_pos[current_image]=0; //set the x coordinate of the first image, by default it goes in the bottom left
    y_pos[current_image]=0; //set the y coordinate of the first image
    lvl_height[0]=image_height[current_image];  //set the height of the first level, same as height of first image into the level
    used_width[0]=image_width[current_image];    //update used width of first level by adding width of image just packed

    for(int i=1;i<num_images;i++){  //for the remaining num_images-1 images
        current_image=images[i];        //choose the image with next highest height

        if(texture_width-used_width[current_lvl] < image_width[current_image] || lvl_height[current_lvl] < image_height[current_image]){ //if the current level is to short or has too little unused width remaining
            current_y+=lvl_height[current_lvl];    //update current_y by adding the height of the previous level
            current_lvl++;  //move to the next level
            lvl_height[current_lvl]=image_height[current_image];    //set the height of the new level based on the height of the current image
        }
            x_pos[current_image]=used_width[current_lvl];   //set the x position of the current image to be as far left as possible in the current level
            y_pos[current_image]=current_y;     //set the y position of the current image to be the y position of the current level
            used_width[current_lvl]+=image_width[current_image];     //update the amount of width already used in the current level by adding the width of the current image
    }
    current_y+=lvl_height[current_lvl];     //calculates the total height of the packing
    return current_y;   //returns the total height of the packing
}

int* sort(minheap h){     //takes as arguements a minheap h to be sorted
    while(!isEmpty(h))  pop(h);    //pops elements until there are none left
    return h->nodes+1;  //when the heap is empty, the array of elements in the heap will be in decreasing order. the 0th node is a sentinel. therefore, we return h->nodes[1:]
}

minheap buildheap(){
    minheap h=(minheap)malloc(sizeof(struct minheap_struct));   //allocates memory for the minheap structure
    h->capacity=num_images;  //sets the max capacity and size of the structure to be equal to the size of the structure
    h->size=num_images;
    h->nodes=(int*)malloc(sizeof(int)*(num_images+1));   //allocates memory for the nodes of the minheap
    h->nodes[0]=-1; //assigns the value -1 to the sentinel node at position 0
    h->nodes[1]=0;  //assigns the address of the 0th image to the root of the minheap, adding the first node to the minheap

    int j, minchild;    //j is an iterator used to travel down the tree while "percolating down". minchild stores the minimum child of node while percolating down
    for(int i=h->size;i>0;i--){
        j=i;    //start at the next empty position in the tree
        while(2*j < h->size){   //while the current node has children
            minchild=2*j;   //assume the left child has smallest height
            if(minchild+1<h->size && image_height[h->nodes[minchild]] > image_height[h->nodes[minchild+1]])     minchild++;   //if the height of the right child is smaller, update minchild
            if(image_height[i-1] > image_height[h->nodes[minchild]]){     //if the height of the node to be inserted is less than the smallest of the heights of its children
                h->nodes[j]=h->nodes[minchild]; //percolate the child up
                j=minchild; //move down a level
            }
            else    break;  //the current node has smaller height than both of its children
        }
        h->nodes[j]=i-1;    //insert the new node at the position found
    }   // !!!NOTE!!! that the values that are stored in the min heap are not the heights of the images, but rather the addresses of each image in the heights and widths arrays. The nodes are sorted however according to their heights.
    return h;   //return the built heap
}

int pop(minheap h){   //takes as arguements a heap h to be popped from

    int temp=h->nodes[h->size]; //saves the last item in the heap
    h->nodes[h->size]=h->nodes[1];  //moves the item at the top of the heap to the former last position in the array which will now be outside of the heap
    h->size--;  //decreases the heap size, excluding the last position in the array from the heap

    int i=1, minchild;  //i is an iterator used to travel down the heap while percolating down, minchild is used to store the child of the current node with smallest height
    //i is set to the top node in the heap
    while(i*2<h->size+1){   //while the current node has children
        minchild=i*2;   //assume the left child has smallest height
        if(minchild<h->size && image_height[h->nodes[minchild]] > image_height[h->nodes[minchild+1]])     minchild++;   //if the height of the right child is smaller, update minchild
        if(image_height[temp] > image_height[h->nodes[minchild]]){      //if the former last node in the array has greater height than both children of the current node
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
