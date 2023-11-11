import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  accountName!: string;
  email!: string;
  password!: string;
  firstName!: string;
  lastName!: string;
  organization!: string;

  constructor(private http: HttpClient, private router: Router) { }
  onSignUpClick() {
    const userData = {
      accountName: this.accountName,
      email: this.email,
      password: this.password,
      firstName: this.firstName,
      lastName: this.lastName,
      organization: this.organization
    };
    console.log('Sending data:', userData);
    // Make a POST request to your Flask API
    this.http.post('http://127.0.0.1:5000/api/register', userData)
      .subscribe(
        (response: any) => {
          if (response.success) {
            // Display success message
            alert(response.message);

            // Redirect to account-page
            this.router.navigate(['/account-page']);
          } else {
            // Display error message
            alert(`Error: ${response.error}`);
          }
        },
        (error) => {
          console.error(error);
          // Handle error, e.g., show an error message to the user
          alert('An error occurred while processing your request.');
        }
      );
  }
}
