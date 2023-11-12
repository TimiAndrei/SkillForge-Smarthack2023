import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent {

  constructor(private router: Router, private http: HttpClient) { }

  picture: string = 'https://i.pravatar.cc/300';



  goToAccount() {
    this.router.navigate(['/account']);
  }

  goToSkill() {
    this.router.navigate(['/addSkill']);
  }

  goToQuest() {
    this.router.navigate(['/addQuest']);
  }

  questBooks: any[] = [
    {
      name: 'Master New Language',
      progress: 0.5,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
    {
      name: 'Coding Guru',
      progress: 0.6,
      deadline: '2021-06-20',
      skills: ['Development', 'Discipline', 'Problem solving', 'Teamwork']

    },
    {
      name: 'Cooking Master',
      progress: 0.2,
      deadline: '2021-07-20',
      skills: ['Cooking fish', 'Baking croissant', 'Making sushi', 'Making pizza']
    },
    {
      name: 'Guitar Master',
      progress: 0.7,
      deadline: '2021-08-15',
      skills: ['Guitar', 'Music', 'Discipline', 'Teamwork']
    },
    {
      name: 'Pitching Master',
      progress: 0.8,
      deadline: '2021-08-20',
      skills: ['Pitching', 'Discipline', 'Communication', 'Teamwork']
    }
  ]

  accordionItems = [
    {
      title: 'Reading',
      content: "Reading is the ability to understand written text and extract meaning from it."
    },
    {
      title: 'Writing',
      content: 'This is the second item\'s accordion body.'
    },
    {
      title: 'Discipline',
      content: 'This is the third item\'s accordion body.'
    }
  ];

  activeIndex: number | null = null;

  toggleAccordion(index: number): void {
    this.activeIndex = this.activeIndex === index ? null : index;
  }




  userName: string = '';

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:5000/api/get-user').subscribe((data: any) => {

      this.userName = data.currentUser.email;

      console.log(data);

    })


    // this.http.get('http://127.0.0.1:5000/api/get-quote').subscribe(
    //   (data: any) => {
    //     // Handle successful response
    //     console.log('Data received:', data);
    //   },
    //   (error: any) => {
    //     // Handle error
    //     const errorMessage = error.error.text;
    //     console.log( errorMessage);

    //     // You can add more specific error handling logic here
    //   }
    // );

  }

}
