import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import {NotificationService, UserService} from '../_services';
import {first} from 'rxjs/operators';


@Component({
  selector: 'app-check-in',
  templateUrl: './check-in.component.html',
  styleUrls: ['./check-in.component.css']
})
export class CheckInComponent implements OnInit {
  checkInForm: FormGroup;
  loading = false;
  submitted = false;
  workoutType = [];
  gymName = [];

  constructor(private formBuilder: FormBuilder,
              private router: Router,
              private notification: NotificationService,
              private userService: UserService) {

  }


  ngOnInit() {
    this.checkInForm = this.formBuilder.group({
     //  gymName: ['', [Validators.required]],
      todaysDate: ['', [Validators.required]],
      workoutType: [''],
      duration: ['', [Validators.required]],
      poundslost: ['', [Validators.required]]


    });
    this.workoutType = [{name: 'Lifting'},
      {name: 'Cardio'}, {name: 'Swimming'}, {name: 'Sports'}, {name: 'Dancing'}  ];
  }

  get f() {
    return this.checkInForm.controls;
  }

  onSubmit() {
    this.submitted = true;
    // stop here if form is invalid
    if (this.checkInForm.invalid) {
      console.log('Error in onSubmit()');
      return;
    }
    this.loading = true;
    this.userService.trackProgress(this.checkInForm.value)
        .pipe(first())
        .subscribe(
            data => {
              //  this.alertService.success('Registration successful', true);
              this.notification.showNotif('Progress Tracked!', 'confirmation');
              this.router.navigate(['/']);
            },
            error => {
              console.log('Error:', error);
              this.notification.showNotif(error);
              this.loading = false;
            });
  }
}
