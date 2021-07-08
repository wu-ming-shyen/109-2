package com.example.menu;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements CompoundButton.OnCheckedChangeListener {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        int[] check_id = {R.id.checkBox1,R.id.checkBox2,R.id.checkBox3,R.id.checkBox4,R.id.checkBox5,R.id.checkBox6,R.id.checkBox7,R.id.checkBox8};

        for(int id:check_id){
            CheckBox check = (CheckBox) findViewById(id);
            check.setOnCheckedChangeListener(this);
        }
    }

    ArrayList<CompoundButton> selected = new ArrayList<>();

    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean isChecked) {
        if (isChecked) {
            selected.add(compoundButton);
        } else {
            selected.remove(compoundButton);
        }
    }

    public void takeOrder(View v){
        String msg = "";

        for(CompoundButton check:selected) msg += "\n" + check.getText();
        msg=msg.length()>0?"你點的餐點是: "+msg:"請點餐!";

        ((TextView) findViewById(R.id.showOrder)).setText(msg);
    }
}