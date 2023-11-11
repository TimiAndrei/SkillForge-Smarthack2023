import { Component, ViewChild } from '@angular/core';
import { RouterModule, Routes, Router } from '@angular/router';
import { ChartType } from 'chart.js';

@Component({
  selector: 'app-account-page',
  templateUrl: './account-page.component.html',
  styleUrls: ['./account-page.component.scss']
})
export class AccountPageComponent {
  
  constructor(private router: Router)
  {
    
  }

  name: string = 'John Doe';
  level: number = 1;
  picture: string = 'https://i.pravatar.cc/300';



  simpleTasks: number = 5;
  mediumTasks: number = 2;
  hardTasks: number = 1;

  radarChartOptions = {
    responsive: true,
    scale: {
      ticks: {
        display: false
      }
    },
    legend: {
      display: false // Set this to false to hide the legend
    }
  };
  radarChartLabels = ['Strength', 'Endurance', 'Speed', 'Agility', 'Flexibility'];

  radarChartData = [
    { data: [80, 70, 20, 50, 35], 
      label: 'John Doe',
      borderColor: '#3cba9f',
      backgroundColor: 'rgba(60,186,159,0.2)',
    },
  ];

  radarChartType: ChartType = 'radar';
  

  goToDashboard() {
    this.router.navigate(['/dashbooard']);
    alert('Dashboard');
        
  }
}




