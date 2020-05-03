import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  serviceUrl: string = ''

  constructor(private http: HttpClient) { }

  x: number = 10;

  search(name: string) {
    if (this.x > 200)
      return "There is no such stock";
    else
      return
  }

}
