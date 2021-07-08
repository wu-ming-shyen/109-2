package com.example.calorie;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    double[] energyRate={3.1,4.4,13.2,9.7,5.1,3.7};
    EditText weight,time;
    TextView total,textViewRate;
    Spinner sports;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        weight= (EditText)findViewById(R.id.weight) ;
        time= (EditText)findViewById(R.id.time);
        total= (TextView)findViewById(R.id.total);
        textViewRate= (TextView)findViewById(R.id.textViewRate) ;
        sports=(Spinner) findViewById(R.id.sports) ;
        sports.setOnItemSelectedListener(this);
    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int position, long id) {
        textViewRate.setText (String.valueOf (energyRate [position])) ;
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }

    public void calc(View v){
        String w = weight.getText().toString();
        String t = time.getText().toString();
        if(w.isEmpty() || w.equals(" .") || t.isEmpty() || t.equals(".")){
            total.setText("請輸入體重及運動時間");
        }
        int pos = sports.getSelectedItemPosition();
        long kcal = Math. round( energyRate[pos] * Double.parseDouble(w) * Double. parseDouble (t));
        total.setText(String.format("消耗能量%d卡",kcal));
    }
}