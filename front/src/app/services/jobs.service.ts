import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../../environments/environment';
import { HttpClient } from '@angular/common/http';
import{ Job } from './../models/job.model'

@Injectable({providedIn:"root"})
export class JobsService {
	constructor(private http:HttpClient){

	}
	getAllJobs():Observable<Job[]>{
		let host = environment.host;
		return this.http.get<Job[]>(host+"/api/jobs")
	}
}