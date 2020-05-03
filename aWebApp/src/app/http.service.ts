import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  serviceUrl: string = ''

  check: object;
  postId: object;


  constructor(private http: HttpClient) { }

  search(stockname: string) {
    this.http.get<any>('http://34.69.143.117:8000/stockinfo/?s=MSFT&r=5d&i=1d', { 'headers': { 'content-type': 'application/json' } }).subscribe(data => {
      console.log(data);
    })

    console.log(name);


    return true;

  }

  getstocks() {
    returnData: Object;
    return this.http.get<any>('http://34.69.143.117:8000/getmassinfo/', { 'headers': { 'content-type': 'application/json' } }).subscribe(data => {
      console.log(data);
      return data;
    })
  }

  getInfo() {

  }

}
