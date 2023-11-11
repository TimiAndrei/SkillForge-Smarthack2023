import { Component, ViewChild } from '@angular/core';
import { RouterModule, Routes, Router } from '@angular/router';

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


  goToDashboard() {
    this.router.navigate(['/dashbooard']);
    alert('Dashboard');
        
  }
}




