#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<iomanip.h>
#include<fstream.h>
#include<stdlib.h>

class persondetails
   {
     int Trvlcode;
     int Trvlrs;
     char Name[30][20];
     int Age[20];
     char Sex[20];
     char Passnum[10][20];
     char Address[50];
     char Phno[20];
     char Familyname[30];
     long double Charges;
     char StartingPoint[20];
     char Destination[20];
     long double Noofdays;
     char Date[20];
     int Children;
     long double totalamount;
     public:
     void input();
     void output();
     void amount();
     int noofchild();
     long double bill();
     void add();
     void display();
     void delrec(int);
     void searchtid(int);
     void searchstartp(char []);
     void searchdest(char []);
   };

void persondetails::input()
   {
     cout<<"Travel Id:";
       {   int v=0;
	   persondetails x;
	    ifstream f("travel.dat",ios::binary);
	    while(f.read((char*)&x,sizeof(x)))
	    {
	     v++;
	    }
	   cout<<v+1;
       }

     cout<<endl<<"Enter the no. of people going:";
     cin>>Trvlrs;

     cout<<"Enter the details :"<<endl;
     for(int i=0;i<Trvlrs;i++)
      {
       cout<<"Traveller "<<i+1<<endl;
       cout<<"Name :";
       gets(Name[i]);
       cout<<"Age :";
       cin>>Age[i];
       cout<<"Gender (M/F) :";
       cin>>Sex[i];
       cout<<"Passport no.:";
       gets(Passnum[i]);
      }

     cout<<"Enter the address:";
     gets(Address);

     cout<<"Enter the phone no. :";
     gets(Phno);

     cout<<"Enter the family name:";
     gets(Familyname);

     cout<<"Enter the starting place:";
     gets(StartingPoint);

     cout<<"Enter the destination:";
     gets(Destination);

     cout<<"Enter start date of journey:  ";
     gets(Date);

     cout<<"Enter no. of days of stay:  ";
     cin>>Noofdays;

     Children=noofchild();
     amount();
     totalamount=bill();

   }

int persondetails::noofchild()
   {
     int x=0;
     for(int i=0;i<Trvlrs;i++)
       {
	 if(Age[i]<11)
	   x++;
       }
     return(x);
   }

long double persondetails::bill()
   {
     long double y;
      y=(Noofdays*(((Charges/2)*Children)+(Charges*(Trvlrs-Children))));
     return(y);
   }

void persondetails::amount()
   {
      if(strcmpi(StartingPoint,"India")==0)
	       {
		 if(strcmpi(Destination,"China")==0)
			   Charges=15000;
		 if(strcmpi(Destination,"Japan")==0)
			   Charges=40000;
		 if(strcmpi(Destination,"Singapore")==0)
			   Charges=60000;
		 if(strcmpi(Destination,"Malaysia")==0)
			   Charges=55000;
		 if(strcmpi(Destination,"Thailand")==0)
			   Charges=50000;
	       }
      else if(strcmpi(StartingPoint,"China")==0)
	       {
		 if(strcmpi(Destination,"India")==0)
			   Charges=15000;
		 if(strcmpi(Destination,"Japan")==0)
			   Charges=20000;
		 if(strcmpi(Destination,"Singapore")==0)
			   Charges=75000;
		 if(strcmpi(Destination,"Malaysia")==0)
			   Charges=70000;
		 if(strcmpi(Destination,"Thailand")==0)
			   Charges=65000;
	       }
      else if(strcmpi(StartingPoint,"Japan")==0)
	       {
		 if(strcmpi(Destination,"India")==0)
			   Charges=40000;
		 if(strcmpi(Destination,"China")==0)
			   Charges=20000;
		 if(strcmpi(Destination,"Singapore")==0)
			   Charges=80000;
		 if(strcmpi(Destination,"Malaysia")==0)
			   Charges=75000;
		 if(strcmpi(Destination,"Thailand")==0)
			   Charges=70000;
	       }
      else if(strcmpi(StartingPoint,"Singaore")==0)
	       {
		 if(strcmpi(Destination,"India")==0)
			   Charges=60000;
		 if(strcmpi(Destination,"China")==0)
			   Charges=75000;
		 if(strcmpi(Destination,"Japan")==0)
			   Charges=80000;
		 if(strcmpi(Destination,"Malaysia")==0)
			   Charges=15000;
		 if(strcmpi(Destination,"Thailand")==0)
			   Charges=20000;
	       }
      else if(strcmpi(StartingPoint,"Malaysia")==0)
	       {
		 if(strcmpi(Destination,"India")==0)
			   Charges=55000;
		 if(strcmpi(Destination,"China")==0)
			   Charges=70000;
		 if(strcmpi(Destination,"Japan")==0)
			   Charges=75000;
		 if(strcmpi(Destination,"Singapore")==0)
			   Charges=80000;
		 if(strcmpi(Destination,"Thailand")==0)
			   Charges=70000;
	       }
      else if(strcmpi(StartingPoint,"Thailand")==0)
	       {
		 if(strcmpi(Destination,"India")==0)
			   Charges=50000;
		 if(strcmpi(Destination,"China")==0)
			   Charges=65000;
		 if(strcmpi(Destination,"Japan")==0)
			   Charges=70000;
		 if(strcmpi(Destination,"Singapore")==0)
			   Charges=20000;
		 if(strcmpi(Destination,"Malaysia")==0)
			   Charges=10000;
	       }
      else if((strcmpi(StartingPoint,"India")==0)&&
	      ( (strcmpi(Destination,"China")!=0)||
		(strcmpi(Destination,"Japan")!=0)||
		(strcmpi(Destination,"Singapore")!=0)||
		(strcmpi(Destination,"Malaysia")!=0)||
		(strcmpi(Destination,"Thailand")!=0)  )
	      )
	    {Charges=0;}
      else if((strcmpi(StartingPoint,"China")==0)&&
	      ( (strcmpi(Destination,"India")!=0)||
		(strcmpi(Destination,"Japan")!=0)||
		(strcmpi(Destination,"Singapore")!=0)||
		(strcmpi(Destination,"Malaysia")!=0)||
		(strcmpi(Destination,"Thailand")!=0)  )
	      )
	    {Charges=0;}
      else if((strcmpi(StartingPoint,"Japan")==0)&&
	      ( (strcmpi(Destination,"India")!=0)||
		(strcmpi(Destination,"China")!=0)||
		(strcmpi(Destination,"Singapore")!=0)||
		(strcmpi(Destination,"Malaysia")!=0)||
		(strcmpi(Destination,"Thailand")!=0)  )
	      )
	    {Charges=0;}
      else if((strcmpi(StartingPoint,"Singapore")==0)&&
	      ( (strcmpi(Destination,"China")!=0)||
		(strcmpi(Destination,"Japan")!=0)||
		(strcmpi(Destination,"India")!=0)||
		(strcmpi(Destination,"Malaysia")!=0)||
		(strcmpi(Destination,"Thailand")!=0)  )
	      )
		Charges=0;
      else if((strcmpi(StartingPoint,"Malaysia")==0)&&
	      ( (strcmpi(Destination,"China")!=0)||
		(strcmpi(Destination,"Japan")!=0)||
		(strcmpi(Destination,"Singapore")!=0)||
		(strcmpi(Destination,"India")!=0)||
		(strcmpi(Destination,"Thailand")!=0)  )
	      )
	 {Charges=0;}
      else if((strcmpi(StartingPoint,"Thailand")==0)&&
	      ( (strcmpi(Destination,"China")!=0)||
		(strcmpi(Destination,"Japan")!=0)||
		(strcmpi(Destination,"Singapore")!=0)||
		(strcmpi(Destination,"Malaysia")!=0)||
		(strcmpi(Destination,"India")!=0)  )
	      )
	   {Charges=0;}
      else if((strcmpi(StartingPoint,"India")!=0)||
	      (strcmpi(StartingPoint,"China")!=0)||
	      (strcmpi(StartingPoint,"Japan")!=0)||
	      (strcmpi(StartingPoint,"Singapore")!=0)||
	      (strcmpi(StartingPoint,"Malaysia")!=0)||
	      (strcmpi(StartingPoint,"Thailand")!=0)
	     )
	{Charges=0;}

   }

void persondetails::output()
  {
    if(Charges!=0)
    {
     cout<<endl<<endl<<endl<<"Travel Id is :"<<Trvlcode<<endl;

     cout<<"No. of people going :"<<Trvlrs<<endl;

     cout<<"Details of members are :"<<endl;
     for(int i=0;i<Trvlrs;i++)
       {
	 cout<<"Name:  "<<Name[i]<<endl;
	 cout<<"  Age:  "<<Age[i]<<endl;
	 cout<<"  Gender:  "<<Sex[i]<<endl;
	 cout<<"  Passport no.:  "<<Passnum[i]<<endl;
       }
     cout<<"Name of family:  ";
      puts(Familyname);
     cout<<"Address :";
      puts(Address);
     cout<<"Phone no.:  ";
      puts(Phno);
     cout<<"Charges are:  "<<Charges;
     cout<<endl<<"Journey is from ";
       puts(StartingPoint);
     cout<<" To ";
       puts(Destination);
     cout<<"Start date of journey:  ";
       puts(Date);
     cout<<endl<<"No. of days of stay:  "<<Noofdays;
     cout<<endl<<"No. of children are:  "<<Children;
     cout<<endl<<"Amount to be paid is:  :"<<totalamount<<endl;
     }
     else
     {
      cout<<"PACKAGE NOT AVAILABLE";
     }
  }

void persondetails::add()
  {
    ofstream f("travel.dat",ios::binary|ios::app);
    persondetails s;
    s.input();
    f.write((char*)&s,sizeof(s));
    f.close();
  }

void persondetails::display()
  {
     persondetails x;
   ifstream f("travel.dat",ios::binary);
   while(f.read((char*)&x,sizeof(x)))
     {
     x.output();
     }
   f.close();
  }

void persondetails::delrec(int w)
  {
    ifstream a("travel.dat",ios::binary);
    ofstream b("t.dat",ios::binary);
    persondetails x;
    while(a.read((char*)&x,sizeof(x)))
     {
      if(x.Trvlcode==w)
	b.write((char*)&x,sizeof(x));
     }
    a.close();
    b.close();
    remove("travel.dat");
    rename("t.dat","travel.dat");
  }

void persondetails::searchtid(int w)
  {
     persondetails x;
   ifstream f("travel.dat",ios::binary);
   while(f.read((char*)&x,sizeof(x)))
     {
       if(x.Trvlcode==w)
	 x.output();
     }
   f.close();
  }

void persondetails::searchstartp(char w[])
  {
     persondetails x;
   ifstream f("travel.dat",ios::binary);
   while(f.read((char*)&x,sizeof(x)))
     {
       if(strcmpi(StartingPoint,w)==0)
	 x.output();
     }
   f.close();
  }

void persondetails::searchdest(char w[])
  {
     persondetails x;
   ifstream f("travel.dat",ios::binary);
   while(f.read((char*)&x,sizeof(x)))
     {
       if(strcmpi(Destination,w)==0)
	 x.output();
     }
   f.close();
  }

void intro()
  {
   char c;
   cout<<"-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#";
   cout<<"\n\t\t\t   VIVEKANAND  SCHOOL\n\n";
   cout<<"-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#";
   cout<<"\n\t\t\t COMPUTER  SCIENCE  PROJECT\n";
   cout<<"\n\t\t\tTopic - CRUISE  MANAGEMENT  SYSTEM\n\n";
   cout<<"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^";
   cout<<"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^";
   cout<<"\n\t\t\t\t  Made by:\n\t\t\t     Shubhangi Bhargava\n";
   cout<<"\t\t\t\tClass 12-C\n\n\n";
   cout<<"********************************************************************************";
   cout<<"\n\n\t\t\t Enter any key to continue\n";
   cin>>c;
   c='1';
   if(c=='1')
   clrscr();
  }

void main()
{ clrscr();
  int n;
  intro();
  do
  {
  clrscr();
  cout<<"********************************************************************************";
  cout<<"\n\n\t\t\tWELCOME  TO  SILVER  SEA  CRUISE\n\n"<<endl;
  cout<<"-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^";
  cout<<"^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-";
  cout<<"********************************************************************************";
  cout<<"\n Enter"<<endl<<
	 "1 : To enter new tour package"<<endl<<
	 "2 : To see previous packages"<<endl<<
	 "3 : To delete a previous package"<<endl<<
	 "4 : To search for a previous package"<<endl<<
	 "5 : To exit"<<endl;
  cin>>n;
  persondetails x;

  if(n==1)
    {
     char c;
     cout<<"Press any key to continue";
     cin>>c;
     c='1';
     if(c=='1')
     clrscr();
     x.add();
    }
  if(n==2)
    {
     char c;
     cout<<"Press any key to continue";
     cin>>c;
     c='1';
     if(c=='1')
     clrscr();
     x.display();
    }
  if(n==3)
    {
     char c;
     cout<<"Press any key to continue";
     cin>>c;
     c='1';
     if(c=='1')
     clrscr();
     int d;
     cout<<"Enter the Travel ID of the package to be deleted:";
     cin>>d;
     x.delrec(d);
    }
  if(n==4)
    {
     char c;
     cout<<"Press any key to continue";
     cin>>c;
     c='1';
     if(c=='1')
     clrscr();

       int m;
       cout<<"\n Enter"<<endl<<
	 "1 : To search by TravelID"<<endl<<
	 "2 : To search byStarting Place"<<endl<<
	 "3 : To search by Destination"<<endl;

       cin>>m;

     if(m==1)
       {
       int y;
       cout<<"Enter the Travel ID of the package:";
       cin>>y;
       x.searchtid(y);
       }
     if(m==2)
       {
       char u[20];
       cout<<"Enter the Starting place of the package:";
       gets(u);
       x.searchstartp(u);
       }
     if(m==3)
       {
       char o[20];
       cout<<"Enter the destination of the package:";
       gets(o);
       x.searchdest(o);
       }
     else
       { cout<<"INVALID SEARCH";
       }
    }
  if(n==5)
    { exit(0);
    }
 }while(n!=5);
 getch();

}