#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
int clientfd, sock = 0, valread;
struct sockaddr_in address;
int opt = 1;
int addrlen = sizeof(address);
char buffer[1024] = { 0 };
char* test = "Test";

int main(){
	if ((clientfd = socket(AF_INET, SOCK_STREAM, 0) == 0)){
		perror("Connection Failed. :( ");
		exit(EXIT_FAILURE);	
	}else{
		printf("Socket file descriptor Sucesss!\n");	
	}
	address.sin_family = AF_INET;
	address.sin_port = htons(PORT);
	if(inet_pton(AF_INET, "127.0.0.1",&address.sin_addr) <= 0){
		printf("\n Invalid address moment \n");
		return -1;	
	}
	if((clientfd = connect(sock,(struct sockaddr*)&address,sizeof(address)))<0){
		perror("connect fail"); exit(EXIT_FAILURE);	
	}
	send(sock,test,strlen(test),0);
	
}
