import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { SingleStockComponent } from './single-stock/single-stock.component';
import { StocksComponent } from './stocks/stocks.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'singlestock', component: SingleStockComponent },
  { path: 'stock', component: StocksComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
