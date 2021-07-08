package com.example.toast;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener {

    String[] queArr = {"什麼門永遠關不上?", "什麼東西沒人愛吃?","什麼瓜不能吃?","什麼布切不斷?","什麼鼠最乾淨?","偷什麼不犯法?"};
    String[] ansArr = {"球門", "虧","傻瓜","瀑布","環保署","偷笑"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_list_item_1,
                queArr);
        ListView lv = (ListView)findViewById((R.id.lv));
        lv.setAdapter(adapter);
        lv.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Toast.makeText(this,"答案:" + ansArr[position],Toast.LENGTH_SHORT).show();
    }
}