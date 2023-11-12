import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent {

  constructor(private router: Router) { }

  picture: string = 'https://i.pravatar.cc/300';



  goToAccount() {
    this.router.navigate(['/account']);
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

    },{
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

    },{
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },{
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },{
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },{
      name: 'The Alchemist',
      progress: 0.7,
      deadline: '2021-05-20',
      skills: ['Reading', 'Writing', 'Speaking', 'Listening']

    },
  ]

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
    }
  ];

  activeIndex: number | null = null;

  toggleAccordion(index: number): void {
    this.activeIndex = this.activeIndex === index ? null : index;
  }





}
