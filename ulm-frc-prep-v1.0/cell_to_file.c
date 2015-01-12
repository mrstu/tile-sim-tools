/*

This program takes as input a series of files in a file list,
each containing a time series of one variable and creates a gridded file
in the same order as the file list.  The command line arguments specify
the file list, the number of timesteps to read at a time, and the outputfile.

*/

/*
Modified 10/23/07
by Deems
to include dynamic memory allocation
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h> 

int main( int argc, char* argv[])
{

  int    i,j,k,m,n, numsteps, numdata, numcells, numtoread, skip, maxstringlength;
  int    flag, remain;
  char   **name;              //name[6500][100];
  char 	 tempname[200], temp[200];
  char 	 outpath[200], tempoutpath[200];
  int 	 *status;
  float  **var;                //var[6500][1000]
  float  junk;
  FILE  *filelist, *gridfile_handle;

  if(argc != 6){
	printf("Wrong command line arguments: enter <filelist> <outfile> <numsteps per chunk> <numdata> <outpath>.\n");
	printf("Expected 6 args.  Given %d args.\n", argc);

	exit(1);
  }

/*open input and output files*/

  filelist=fopen(argv[1], "r");
  printf("filelist: %s\n",argv[1]);

  if(filelist==NULL) printf("cannot open filelist %s\n", argv[1]);
  gridfile_handle=fopen(argv[2], "r");


sscanf(argv[3],"%d", &numsteps);
sscanf(argv[4],"%d", &numdata);
printf("numsteps %d\n",numdata);
sscanf(argv[5],"%s", &outpath);
printf("outpath: %s\n",outpath);
strcpy(tempoutpath, outpath);
//printf("outfile: %s\n",argv[5]);


/* Initialize variables */

 skip = 0;
 flag = 0;
 remain = numdata;
 maxstringlength = 200;

 if(numsteps > numdata)  numtoread = numdata;
 else  numtoread = numsteps;

fscanf(filelist, "%d", &numcells);         //number of cells is on first line of file list file
 printf("%d\n", numcells);

// FILE *workfile[numcells];
 FILE **workfile = malloc(sizeof(FILE*) * (numcells-1));

/*Allocate memory for large arrays*/

  var = (float **)malloc(numcells * sizeof(float*));  
                                     
  for(i=0;i<numcells;i++){ 
    var[i] = (float *)malloc(numtoread  * sizeof(float));  
    
    }

  status = malloc(numcells * sizeof(int));

  name = (char **)malloc(numcells * sizeof(char*));

  for(i=0;i<numcells;i++){
    name[i] = (char *)malloc(maxstringlength * sizeof(char));
    }


 for(i=0;i<numcells;i++){ 

//    fscanf(filelist, "%s %d",name[i],&status[i]);
    fscanf(filelist, "%s",name[i]);
    fscanf(filelist, "%d",&status[i]);
/*
//    strcat(tempoutpath,"/");
    strcpy(tempoutpath,outpath);
    strcat(tempoutpath,temp);
//    strcpy(name[i],tempoutpath)
    name[i] = tempoutpath;
*/
//    printf("outfile: %s\n",name[i]);
/*
	workfile[i]=fopen(tempoutpath, "w+"); // TODO: need to allocate file pointer array
//	workfile[i]=fopen(name[i], "w"); // TODO: need to allocate file pointer array
	if(workfile[i]==NULL) {
		printf("cannot open workfile %d %s\n", i, name[i]);
		exit(0);
	}
*/

    //    printf("workfile: %s\n",name[i]);
//    strcpy(tempoutpath,outpath);

//    fscanf(filelist, "%s",name[i]);

//   fscanf(filelist, "%s",tempname);
//   name[i] = strcat(temp, name[i]);
   /*printf("%d  %s\n",i,name[i]);*/

  }

// for(i=0;i<numcells;i++){
//     printf("outfile: %d, %s\n",i,name[i]);
//   }


fclose(filelist);
//exit(0);

/*read argument strings to integer values*/
  printf("Here\n");


/* Main Loop */
 printf("Main Loop\n\n");

//gridfile_handle=fopen(grid, "r"); //TODO: expects a vector... need to pass in array

// open files for writing out data.
/*for(i=0;i<numcells;i++) {
	printf("file to open: %s\n", name[i]);
	workfile[i]=fopen(name[i], "wb"); // TODO: need to allocate file pointer array
    if(workfile[i]==NULL) printf("cannot open %s\n", name[i]);
	}*/

 while(numtoread > 0){
	printf("Reading. %d timesteps remain.\n\n", remain);
	for(k=0;k<numtoread;k++){
		for(i=0;i<numcells;i++){

//	workfile=fopen(name[i], "r"); // moved to before while
//data_48.34375_-113.40625

/* skip records in beginning of working file*/

//	for(j=0;j<skip;j++) fscanf(gridfile, "%f", &junk);
	   //	for(j=0;j<skip;j++) fscanf(gridfile, "%f", &junk);


/* load array with numtoread timesteps */

			fscanf(gridfile_handle, "%f", &var[i][k]);
//			printf("%3.1f\n", var[i][k]);

//	fclose(workfile);

		 	}
		}

/* print out data chunk to the output file */
		printf("Writing. %d timesteps remain.\n\n", remain);
		for(n=0;n<numcells;n++){
			if(status[n]==1){

				if(remain==numdata){
					sscanf("w+","%s", &tempname);
					//				tempname="w";
					}
				else{
					sscanf("a+","%s", &tempname);
					//				tempname="a";
					}

				//    strcat(tempoutpath,"/");
				strcpy(tempoutpath,outpath);
				strcat(tempoutpath,name[n]);
			//    strcpy(name[i],tempoutpath)
	//			name[i] = tempoutpath;
	//			printf("file to open: %s\n", tempoutpath);
				workfile[n]=fopen(tempoutpath, tempname); // TODO: need to allocate file pointer array
	//			printf("%s\n", name[n]);
	//			if(workfile[n]==NULL) printf("cannot open workfile %s\n", name[n]);
				if(workfile[n]==NULL) {
					printf("cannot open workfile %d %s\n", n, name[n]);
					exit(1);
				}

	//		    junk = 0;
				for(m=0;m<numtoread;m++){
	//				if(var[n][m]>0) junk+=var[n][m];
	////				if(var[n][m]>0) printf("%s, %f\n", name[n],var[n][m]);
	//				printf("vals %3.1f\n,", var[n][m]);
					fprintf(workfile[n], "%3.2f\n", var[n][m]);
					}
	//			if(junk>0) printf("%s, %f\n", name[n],junk);

				//	fprintf(outputfile, "\n");

				fclose(workfile[n]);
			}
		}
		skip += numsteps;
		remain = numdata-skip;

		if(remain >= numsteps) numtoread = numsteps;
		else if(remain <= 0) numtoread = 0;
		else numtoread = remain;
		printf("Remaing records: %d\n\n", remain);
 	}

 	return 0;
/*
for(i=0;i<numcells;i++) {
	fclose(workfile[i]);
	}
*/


}
