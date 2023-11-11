import { RouterModule, Routes, Router } from '@angular/router';
import { Component, ViewChild, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-account-page',
  templateUrl: './account-page.component.html',
  styleUrls: ['./account-page.component.scss']

})


export class AccountPageComponent implements OnInit {
  apiURL = 'http://127.0.0.1:5000/api/test';
  responseData: any;

  name: string = 'John Doe';
  level: number = 1;
  picture: string = 'https://i.pravatar.cc/300';

  constructor(private http: HttpClient , private router: Router) { }

  goToDashboard() {
    this.router.navigate(['/dashbooard']);
    alert('Dashboard');
        
  ngOnInit(): void {
    this.http.get(this.apiURL)
      .subscribe((data: any) => {
        this.responseData = data;
        console.log(this.responseData);
      });
  }
}





