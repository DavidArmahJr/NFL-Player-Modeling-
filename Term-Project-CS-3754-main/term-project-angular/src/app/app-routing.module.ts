import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {DashboardComponent} from './dashboard/dashboard.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {Role} from './_models/role';
import {AuthGuard} from './_guards/auth.guard';
import {AdminComponent} from './admin/admin.component';
import {GymCreatorComponent} from "./gym-creator/gym-creator.component";
import {CheckInComponent} from "./check-in/check-in.component";
import {UserInfoComponent} from "./user-info/user-info.component";
import {LeaderboardComponent} from "./leaderboard/leaderboard.component";


//TODO: do not forget to register the components here.

const routes: Routes = [{path: '', component: DashboardComponent, canActivate: [AuthGuard]}, {path: 'login', component: LoginComponent},
  { path: 'register', component: RegisterComponent },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard],
    // The prof route also sets the roles data property to [Role.professor] so only admin users can access it.
    data: { roles: [Role.trainer] }
  },

  {
    path: 'gymCreator',
    component: GymCreatorComponent,
    canActivate: [AuthGuard],
    // The prof route also sets the roles data property to [Role.Admin] so only admin users can access it.
    data: { roles: [Role.trainer] }
  },
  {
    path: 'track',
    component: CheckInComponent,
    canActivate: [AuthGuard],
    // The prof route also sets the roles data property to [Role.Admin] so only admin users can access it.
    data: { roles: [ Role.member] }
  },
  {
    path: 'userinfo',
    component: UserInfoComponent,
    canActivate: [AuthGuard],
    // The prof route also sets the roles data property to [Role.Admin] so only admin users can access it.
    data: { roles: [Role.member] }
  },
  {path: 'leaderboard',
    component: LeaderboardComponent,
    canActivate: [AuthGuard],
    // The prof route also sets the roles data property to [Role.Admin] so only admin users can access it.
    data: { roles: [Role.member, Role.trainer] }},


{ path: '**', redirectTo: '' }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
