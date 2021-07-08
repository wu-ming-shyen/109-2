package com.example.menu_pro;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ListView l = (ListView)findViewById(R.id.listView);
        l.setOnItemClickListener(this);
    }

    ArrayList<String> selected = new ArrayList<>();

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int position, long id) {
        TextView t = (TextView) view;
        String item = t.getText().toString();

        if(selected.contains(item))
            selected.remove(item);
        else
            selected.add(item);

        String msg;

        if (selected.size()>0){
            msg = "你點了:";
            for(String str:selected)
                msg+=" "+str;
        }
        else
            msg = "請點餐!";

        TextView textView = (TextView)findViewById(R.id.textView);
        textView.setText(msg);
    }
}