import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  signUpForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {
    this.signUpForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      accountName: ['', Validators.required],
      password: ['', Validators.required],
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      organization: ['']
    });
  }

  redirectToLogin() {
    this.router.navigate(['/login2']);
  }

  async onSignUpClick() {
    if (this.signUpForm.valid) {
      const userData = this.signUpForm.value;

      console.log('Sending data:', userData);

      try {
        const response: any = await this.http.post('http://127.0.0.1:5000/api/register', userData).toPromise();

        if (response.success) {
          // Display success message
          alert(response.message);

          // Redirect to account-page
          this.router.navigate(['/account']);
        } else {
          // Display error message
          alert(`Error: ${response.error}`);
        }
      } catch (error) {
        console.error(error);
        // Handle error, e.g., show an error message to the user
        alert('An error occurred while processing your request.');
      }
    }
  }
}
