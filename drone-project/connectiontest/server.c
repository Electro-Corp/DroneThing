#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
int serverfd, serversocket, valread;
struct sockaddr_in address;
int opt = 1;
int addrlen = sizeof(address);
char buffer[1024] = { 0 };
char* test = "Test";

//function decleration
void setupSocket(void);
void readdata(void);
int main(int argc, char const* argv[]){

	setupSocket();
	readdata();
	
	close(serversocket);
	shutdown(serverfd, SHUT,RDWR);
	return 0;
}
void setupSocket(){
	if ((serverfd = socket(AF_INET, SOCK_STREAM, 0) == 0)){
		perror("Connection Failed. :( ");
		exit(EXIT_FAILURE);	
	}else{
		printf("Socket file descriptor Sucesss!\n");	
	}
	serverfd = socket(AF_INET, SOCK_STREAM, 0);
	//force to port 8080
	if(setsockopt(serverfd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))){
		perror("Set socket port fail!");
		exit(EXIT_FAILURE);	
	}
	setsockopt(serverfd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);
	
	//bind(serverfd,(struct sockaddr*)&address, sizeof(address));
	if(bind(serverfd,(struct sockaddr*)&address, sizeof(address)) < 0){
		perror("Bind fail!");
		exit(EXIT_FAILURE);	
	}
	if(listen(serverfd,3) <0){
		perror("listen fail"); exit(EXIT_FAILURE);
	}
	if((serversocket = accept(serverfd,(struct sockaddr*)&address, (socklen_t*)&addrlen))<0){
		perror("accept fail"); exit(EXIT_FAILURE);	
	}
	
}
void readdata(){
	valread = read(serversocket,buffer,1024);
	printf("%s\n",buffer);
}
