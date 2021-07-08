package com.example.memo_pro;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener, AdapterView.OnItemLongClickListener{

    String [] aMemo = {"1.按一下可以編輯備忘","2.長按可以清除備忘","3.","4.","5.","6."};
    ListView lv;
    ArrayAdapter<String> str;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        lv = (ListView)findViewById(R.id.listView);
        str = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1,aMemo);

        lv.setAdapter(str);

        lv.setOnItemClickListener(this);
        lv.setOnItemLongClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> a, View view, int position, long id) {
        Intent it = new Intent(this,Edit.class);
        it.putExtra("備忘",aMemo[position]);
        startActivityForResult(it,position);

    }

    @Override
    public boolean onItemLongClick(AdapterView<?> a, View view, int position, long id) {
        aMemo[position] = (position+1) + ".";
        str.notifyDataSetChanged();
        return false;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode,Intent it) {
        super.onActivityResult(requestCode, resultCode, it);
        if (resultCode == RESULT_OK) {
            aMemo[requestCode] = it.getStringExtra("備忘");
            str.notifyDataSetChanged();
        }
    }
}