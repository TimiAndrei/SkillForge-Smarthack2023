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
      name: 'The Alchemist',
      progress: 0.5,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
    {
      name: 'The Alchemist',
      progress: 0.6,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
    {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
    {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    }, {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
    {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    }, {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    }, {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    }, {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    }, {
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
  ]

  

  activeIndex: number | null = null;

  toggleAccordion(index: number): void {
    this.activeIndex = this.activeIndex === index ? null : index;
  }


  errorMessage: string = '';


  userName: string = '';

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:5000/api/get-user').subscribe((data: any) => {

      this.userName = data.currentUser.email;

      console.log(data);

    })

    this.http.get('http://127.0.0.1:5000/get-skill-suggestion').subscribe(
      (data: any) => {
        // Handle successful response
        console.log('Data received:', data);
      },
      (error: any) => {
        // Handle error
        this.errorMessage = error.error.text;

        console.log( this.errorMessage);


        //find out the last index of accordion items, and set its title to the error message
        let lastItemIndex = this.accordionItems.length - 1;
        // the title should be everything until the second " character
        let title = this.errorMessage.substring(0, this.errorMessage.indexOf('"', 2) + 1);
        // the content should be everything after the second " character
        let content = this.errorMessage.substring(this.errorMessage.indexOf('"', 2) + 1);
        
        this.accordionItems[lastItemIndex].content = content;




        
      }
    );

  }


  accordionItems = [
    {
      title: 'Accordion Item #1',
      content: 'This is the first item\'s accordion body.'
    },
    {
      title: 'Accordion Item #2',
      content: 'This is the second item\'s accordion body.'
    },
    {
      title: 'Accordion Item #3',
      content: 'This is the third item\'s accordion body.'
    },
    {
      title: 'More Suggestions',
      content: 'Waiting for more suggestions...'
    }
  ];

}
