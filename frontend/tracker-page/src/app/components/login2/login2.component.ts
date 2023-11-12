import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login2',
  templateUrl: './login2.component.html',
  styleUrls: ['./login2.component.scss']
})
export class Login2Component {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {
    this.loginForm = this.fb.group({
      accountName: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  redirectToSignUp() {
    this.router.navigate(['/login']);
  }

  // Modify the function to include the token in the request headers
  async onLoginClick() {
    if (this.loginForm.valid) {
      const loginData = this.loginForm.value;

      console.log('Sending login data:', loginData);

      try {
        const response: any = await this.http.post('http://127.0.0.1:5000/api/login', loginData).toPromise();

        if (response.success) {
          // Display success message
          alert(response.message);

          // Save the token to localStorage
          sessionStorage.setItem('token', response.token);

          // Redirect to account-page
          this.router.navigate(['/account']);

        } else {
          // Display error message
          alert(`Error: ${response.error}`);
        }
      } catch (error) {
        console.error(error);
        // Handle error, e.g., show an error message to the user
        alert('An error occurred while processing your login request.');
      }
    }
  }

}
