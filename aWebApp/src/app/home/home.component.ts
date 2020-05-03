import { Component, OnInit } from '@angular/core';

import { HttpService } from '../http.service';
import { Router } from '@angular/router';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  stockname: any = "MSFT";

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
  }

  search(): any {
    
    console.log(AppComponent.stocksymbol)
    AppComponent.stocksymbol = this.stockname
    this._http.search(AppComponent.stocksymbol.toString()).subscribe(data => {
      if (data.status === undefined) {
        this.router.navigate(['/singlestock'])
      }
    });
  }
}