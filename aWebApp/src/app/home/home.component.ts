import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';
import { SingleStockComponent } from '../single-stock/single-stock.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  stockname: string = '';

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
  }

  search(): void {
    this._http.search(this.stockname).subscribe(data => {
      if (data.status === undefined)
        this.router.navigate(["/singlestock"]);
    })
  }

}
