import { RouterModule, Routes, Router } from '@angular/router';
import { ChartType } from 'chart.js';
import { Component, ViewChild, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-account-page',
  templateUrl: './account-page.component.html',
  styleUrls: ['./account-page.component.scss']

})


export class AccountPageComponent implements OnInit {

  constructor(private http: HttpClient, private router: Router) { }

  apiURL = 'http://127.0.0.1:5000/api/test';
  responseData: any;

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
  
  constructor(private http: HttpClient , private router: Router) { }


  ngOnInit(): void {
    this.http.get(this.apiURL)
      .subscribe((data: any) => {
        this.responseData = data;
        console.log(this.responseData);
      });
  }

  goToDashboard() {
    this.router.navigate(['/dashbooard']);
    alert('Dashboard');
  }
}


